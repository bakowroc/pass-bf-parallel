import dispy

from compute import compute
from utils import generate_strings


class Master:
    def __init__(self, password):
        self._password = password
        self._cluster = dispy.JobCluster(computation=compute, callback=self.job_callback)
        self._jobs = []

    def start(self):
        batch = []

        for index, string in enumerate(generate_strings(len(self._password))):
            batch.append(string)
            if len(batch) == 20:
                job = self._cluster.submit([self._password, batch])
                job.id = index
                self._jobs.append(job)
                batch = []

    def job_callback(self, job):
        if job.status == dispy.DispyJob.ProvisionalResult:
            if job.result[2]:
                print(f'{job.result[0]} in JOB {job.id} found solution! It\'s {job.result[1]}')

                for j in self._jobs:
                    if j.status in [dispy.DispyJob.Created, dispy.DispyJob.Running, dispy.DispyJob.ProvisionalResult]:
                            self._cluster.cancel(j)
