import dispy

from compute import compute
from utils import generate_strings


class Master:
    def __init__(self, password):
        self._password = password
        self._cluster = dispy.JobCluster(nodes=['10.11.220.20', '10.11.220.21', '10.11.220.22', '10.11.220.23'],
                                         computation=compute,
                                         callback=self.job_callback)
        self._jobs = []
        self._finished = False

    def start(self):
        batch = []
        job_id = 1
        for index, string in enumerate(generate_strings(len(self._password))):
            if self._finished:
                break

            batch.append(string)
            if len(batch) == 20:
                job = self._cluster.submit([self._password, batch])
                job.id = job_id
                self._jobs.append(job)

                job_id += 1
                batch = []

        self._cluster.wait()
        self._cluster.print_status()

    def job_callback(self, job):
        if job.status == dispy.DispyJob.ProvisionalResult:
            if job.result[2]:
                print(f'{job.result[0]} in JOB {job.id} found solution! It\'s {job.result[1]}')
                self._finished = True
                self._cluster.close(terminate=True)
                # for j in self._jobs:
                #     if j.status in [dispy.DispyJob.Created, dispy.DispyJob.Running, dispy.DispyJob.ProvisionalResult]:
                #         try:
                #             self._cluster.cancel(j)
                #         except ValueError:
                #             pass
