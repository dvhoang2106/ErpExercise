from array import *

def tinhmuy(data):
    m = 0
    dtrain = 0
    #duyet mang neu ptu khac -1 (tuc la ptu chua danh nhan) thi cong no zo va tang dtrain len 1 
    for a in data :
        for b in a :
            if (b != -1):
                dtrain  = dtrain +1
                m = m + b
    m = m / dtrain
    # muy = tong cua tat ca cac phan tu khac -1 chia cho dtrain
    return m 
#ham tinh b_u va b_i
def tinhb(array , m):
    b = 0
    dtrain = 0
    for a in array:
        if(a != -1):
            b = b+ (a - m)
            dtrain = dtrain + 1
            #duyet mang neu ptu khac -1 thi tang dtrain len 1, lay phan tu do tru  muy
            #b = tong cac phan tu tru muy da tinh 
    return(b / dtrain)

if __name__ == "__main__":
    data =  [
    [1 , 4, 5, -1, 3],
    [5 , 1, -1, 5, 2],
    [4 , 1, 2, 5, -1],
    [-1 , 3, 4, -1, 4]
    ]
    muy = tinhmuy(data) 
    print(tinhmuy(data) )
    B = [1 , 4, 5, -1, 3]
    print(tinhb(B, tinhmuy(data)))

    for u in range(len(data)):
        for i in range(len(data[0])):
            if(data[u][i] == -1):
                cols=list(zip(*data))
                b_u = tinhb(data[u],muy)
                b_i = tinhb(cols[i],muy)
                data[u][i] = muy+ b_u + b_i
    print(data)
        
