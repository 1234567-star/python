num_of_input=int(input())
product_samples=[]
cost_of_product=[]
tax_for_the_product=[]

i=0
for i in range (num_of_input):
    product_id,cost_of_unit_product,tax_of_unit_product=map(float,input().split("|"))
    product_samples.append(product_id)
    cost_of_product.append(cost_of_unit_product)
    tax_for_the_product.append(tax_of_unit_product)
num_of_product=int(input())



j=0
for j in range (num_of_product):
    purchased_product,count=map(float,input().split("|"))
    print("******************START BILL*********************")
    x=product_samples.index(purchased_product)
    if purchased_product in product_samples:
        cost_of_purchased_product=cost_of_product[x]*count
        total_tax=tax_for_the_product[x]*count
        net_total=cost_of_purchased_product+total_tax
        print(f"{purchased_product}|{cost_of_product[x]}|{cost_of_purchased_product}|{tax_for_the_product[x]}|{total_tax}|{net_total}")

    
print("***********************END BILL*******************")






























