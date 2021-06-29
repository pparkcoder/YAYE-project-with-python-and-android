food = {'gim':1, 'kimchi':2, 'kimchijeon':3, 'kimchijigae':4, 'dakgalbi':5, 'doenjangjjigae':6, 'tteokbokki':7, 'myeolchibokkeum':8, 'miyeoggug':9,
        'Sausage Jeon':10, 'sundubujjigae':11, 'sigeumchi':12, 'eomug bokk-eum':13, 'jeyug':14, 'kongnamulgug':15, 'kongnamulmuchim':16}

for j in range(len(list(food.keys()))):
    for i in range(1, 500):
        try:
            text_file_path = 'C:/darknet-master/build/darknet/x64/train_data/img/{0} ({1}).txt'.format(list(food.keys())[j], i)

            with open(text_file_path,'r') as f:
                lines = f.readlines()
                new_text_content = str(food[list(food.keys())[j]]) + lines[0][1:]

            with open(text_file_path,'w') as f:
                f.write(new_text_content)
        except:
            pass
