from flask import Flask, request, jsonify
import datetime


app = Flask(__name__)

@app.route('/delivery_fee', methods=['POST'])
def delivery_fee():
    data = request.get_json()
    cart_value = data['cart_value']
    delivery_distance = data['delivery_distance']
    num_items = data['number_of_items']
    time = data['time']

    if cart_value >= 10000:
        delivery_fee = 0
    else:        
        if delivery_distance > 1000:
            delivery_fee = 200
            extra_distance = delivery_distance - 1000
            extra_fee = (extra_distance // 500)*100 + (100 if extra_distance % 500 else 0)
            #if extra_distanse divided by 500 has remainder add 1 to floor division of extra_distance and 500 
            delivery_fee += extra_fee
            
        if num_items >= 5:
            additional_items = num_items - 4
            extra_fee = additional_items * 50 
            #for each additional item add 0.5
            if num_items >= 12:
                extra_fee+=120
            delivery_fee += extra_fee
            
        if cart_value < 1000:
            delivery_fee += 1000 - cart_value
            
        date_given = time[0:10]
        date_component = datetime.datetime.strptime(date_given, "%Y-%m-%d").date()
        day_name = date_component.strftime("%A") 
        #find the week day name 
        
        if day_name=='Friday':
            date_comp = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S%z")
            utc_zone = date_comp.astimezone(datetime.timezone.utc)
            hour = utc_zone.hour
            if 15<=hour<19:
                delivery_fee = delivery_fee* 1200
            #if friday find the if it is in rush hour and multiply the delivery fee .2
                
        delivery_fee = min(delivery_fee, 1500)
        
    return jsonify({'delivery_fee': delivery_fee})

if __name__ == '__main__':
    app.run(debug=True)
