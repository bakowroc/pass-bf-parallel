import dispy
import sys

from compute import compute
from utils import generate_strings


class Master:
    def __init__(self, password, nodes, partioning=1):
        self._nodes = nodes
        self._password = password
        self._cluster = dispy.JobCluster(nodes=self._nodes,
                                         computation=compute,
                                         callback=self.job_callback)
        self._jobs = []
        self._solution_report = {}
        self._finished = False
        self._partioning = len(self._password) - partioning
        self._finished_time = 0

        if partioning == 0:
            raise Exception('Partioning has to be larger than 0')

        if partioning >= len(self._password):
            raise Exception('Partioning has to be smaller than password length')

    def start(self):
        job_id = 1
        for base_string in generate_strings(length=len(self._password) - self._partioning):
            if self._finished:
                self._cluster.close(terminate=True)
                break

            job = self._cluster.submit([self._password, base_string])
            job.id = job_id
            self._jobs.append(job)
            job_id += 1

        self._cluster.wait()
        self.save_status()

    def save_status(self):
        file_name = f'{self._password}_{self._partioning}_{len(self._nodes)}'
        orig_stdout = sys.stdout
        f = open("./TESTS/" + file_name, 'w+')
        f.write(f"SLAVE: {self._solution_report['slave']}\n")
        f.write(f"JOB:  {self._solution_report['job']}\n")
        f.write(f"SOLUTION: {self._solution_report['solution']}\n")
        f.write("SUMMARY: \n")
        sys.stdout = f
        self._cluster.print_status()

        sys.stdout = orig_stdout
        f.close()
        print('FINISHED')

    def job_callback(self, job):
        if job.status == dispy.DispyJob.ProvisionalResult:
            if job.result[2]:
                self._solution_report = {
                    'slave': job.result[0],
                    'job': job.id,
                    'solution': job.result[1]
                }
                self._finished = True
