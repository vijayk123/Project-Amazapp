# IAM AccessDenied error while creating EKS cluster

## What happened
When I tried to create an EKS cluster using eksctl, I got this error:

AccessDeniedException: not authorized to perform eks:DescribeClusterVersions

The cluster creation stopped immediately.

---

## Why this happened
I was using an IAM user that I had created earlier for CI/CD.

That user had permissions for:
- Pushing Docker images to ECR

But it did NOT have permissions for:
- EKS
- EC2
- VPC
- IAM

So eksctl could not even check supported EKS versions.

---

## Important realization
CI/CD users and infrastructure users should **never be the same**.

In real companies:
- CI users are restricted
- Infra admins have broader permissions
- Mixing them is a security risk

---

## Fix I applied
1. Switched to a separate IAM user for infrastructure work
2. Attached admin-level permissions temporarily
3. Reconfigured AWS CLI with the new user
4. Verified identity using:

aws sts get-caller-identity

After this, eksctl worked correctly.

---

## Final result
- EKS cluster was created successfully
- CI user remained restricted to ECR only

---

## What I learned
IAM errors are usually **correct behavior**, not AWS problems.

AWS was protecting the account from misuse.

---
