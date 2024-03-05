#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, job=""):
        self.job = ""
        self.job = job

    def job(self):
        return self._job

    def job(self, value):
        if value in self.approved_jobs:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
            print("The job must be in the following list of jobs:")
            print(self.approved_jobs)

person1 = Person("ICT")
print(person1.job)