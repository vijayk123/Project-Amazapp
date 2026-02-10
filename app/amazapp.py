from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return f"E-commerce backend running on pod: {socket.gethostname()}\n"



# Health check (VERY IMPORTANT)
@app.route("/health")
def health():
    return jsonify(status="UP"), 200

# Sample products (mock DB)
products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Phone", "price": 30000}
]

@app.route("/products")
def get_products():
    return jsonify(products)

#@app.route("/")
#def home():
#    return "E-commerce backend running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
