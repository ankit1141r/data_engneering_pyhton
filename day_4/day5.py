import requests
def productprice(product_id):
  products=requests.get("https://fake-store-api.mock.beeceptor.com/api/products").json()
  for product in products:
    if product['product_id']==product_id:
      return float(product["price"])-float(product['discount'])
def cartvalue():
  carts=requests.get("https://fake-store-api.mock.beeceptor.com/api/carts").json()
  total=0
  for cart in carts:
      for item in cart['items']:
        price=productprice(item['product_id'])
        total+=price*item['quantity']
  return total   
print("total cart value",cartvalue())