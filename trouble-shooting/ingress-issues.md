# Ingress issues – Understanding LoadBalancer vs Ingress the hard way

## What I saw
My application pods were running and the service existed, but I couldn’t access the app in the browser.

Sometimes:
- I could access the LoadBalancer IP
- Sometimes Ingress returned 404 or 503
- Sometimes nothing worked

This was confusing at first.

---

## What I misunderstood initially
I assumed:
- Ingress could directly forward traffic to pods
- Creating Ingress alone was enough

That assumption was wrong.

---

## Real traffic flow (important)
Ingress does NOT talk to pods directly.

The correct flow is:

Browser  
→ LoadBalancer (Ingress Controller)  
→ Ingress rules  
→ Service  
→ Pods  

If **Service is missing or selectors don’t match**, Ingress has nowhere to send traffic.

---

## How I debugged it
I checked:
- kubectl get ingress
- kubectl get svc
- kubectl get endpoints <service-name>

That’s when I noticed:
- Service existed, but
- Endpoints were empty due to label mismatch

This explained why Ingress was failing.

---

## Fix I applied
- Fixed Service selector to match pod labels
- Ensured Ingress backend pointed to Service (not pod)
- Used the **Ingress Controller LoadBalancer external IP**, not pod IPs

---

## Final result
- Application became accessible through Ingress
- Traffic was routed correctly to pods
- Browser access worked consistently

---

## What I learned
Ingress is only a **routing layer**.

Service is mandatory.
No Service = no traffic.

---