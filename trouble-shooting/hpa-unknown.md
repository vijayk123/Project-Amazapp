# HPA CPU showing `<unknown>` – What went wrong and how I fixed it

## What I saw
I created an HPA for my amazapp deployment, but when I checked it using:

kubectl get hpa

the CPU metric was showing:

cpu: <unknown> / 50%

Because of this, pods were not scaling at all.

---

## Initial confusion
At first, I thought:
- Maybe my deployment YAML was wrong
- Maybe CPU requests were missing
- Maybe HPA itself was broken

But the HPA object was created successfully, so the problem had to be somewhere else.

---

## Actual root cause
HPA does not calculate CPU usage by itself.

It depends on **metrics-server** to get CPU and memory metrics from the nodes.

In my EKS cluster:
- metrics-server was either not installed or
- installed but unable to talk to kubelets because of TLS issues

As a result, Kubernetes had no CPU data to give to HPA, so it showed `<unknown>`.

---

## How I verified the issue
I ran:

kubectl top pods

This command failed, which confirmed that metrics were not available at all.

---

## Fix I applied
1. Installed metrics-server using the official manifest.
2. Edited the metrics-server deployment and added EKS-compatible flags:
   - --kubelet-insecure-tls
   - --kubelet-preferred-address-types=InternalIP
3. Waited for the metrics-server pod to restart.

After that, `kubectl top pods` started showing CPU and memory values.

---

## Final result
- HPA started showing real CPU values
- Pods scaled up when load increased
- Pods scaled down when load stopped

---

## What I learned
HPA problems are often **metrics problems**, not scaling problems.

If CPU shows `<unknown>`, always check:
- metrics-server
- kubelet communication
- `kubectl top`

---

