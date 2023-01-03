#inisialisasi list
petak_sawah = []

from PIL import Image as PImage
import numpy as np
import matplotlib.pyplot as plt

#def filetext untuk membaca file text
def baca_data(fileteks):
    file = open(fileteks, "r")
    text = file.readlines()

    global counter
    counter = 0
    for i in text:

        data = i.split()
        lokasi = data[0]
        hari = int(data[1])
        berat = float(data[2])
        harga = int(data[3])
        petak_sawah.append({'Lokasi' : lokasi, 'Hari Panen' : hari, 'Berat Gabah' : berat, 'Harga per kg' : harga})
        counter +=1
    return petak_sawah


#def print_data untuk membuat list data dari dict agar nyaman dilihat
def print_data(x):
    for elemen in x:
        for k,v in elemen.items():
            print(k ,'=',v)
        print('\n')


       
#def report untuk menampilkan total gabah dan total penjualan selama setahun        
def report():
    counter_r = 0
    while counter_r < counter:
        data_dict = petak_sawah[counter_r]
        lokasi = data_dict['Lokasi']
        hari = data_dict['Hari Panen']
        berat = data_dict['Berat Gabah']
        harga = data_dict['Harga per kg']

        while hari+data_dict['Hari Panen'] < 365:
            berat = berat + data_dict['Berat Gabah']
            hari = hari + data_dict['Hari Panen']

        counter_r += 1
        hasil = (berat*1000)*harga
        hasil2 = hari / data_dict['Hari Panen']
        hasil3 = round(hasil * hasil2)
        
        print ('Lokasi :', lokasi, '\nTotal Gabah :',berat, 'Ton\nTotal Penjualan :', hasil3,'Rupiah\n')

#def rerata untuk mencari rata-rata hasil panen
def rerata(n):
    counter_rerata = 0
    list_lokasi = []
    dict_produksi = {}
    temp = []

    while counter_rerata < counter:
        data_dict = petak_sawah[counter_rerata]
        lokasi = data_dict['Lokasi']

        berat = data_dict['Berat Gabah']   
        if lokasi not in dict_produksi:
            dict_produksi[lokasi]=berat
        elif lokasi in dict_produksi:
            if not temp:   
                temp.append(dict_produksi[lokasi])
            temp.append(berat)
            dict_produksi[lokasi] = temp
        list_lokasi.append(lokasi)
        counter_rerata += 1
    if n in list_lokasi:
        try:
            rerata = round(sum(dict_produksi[n])/len(dict_produksi[n]),2)
            return rerata
        except TypeError:
            rerata = (dict_produksi[n])
            return rerata
        
    else:
        return "Input tidak valid"

#def produktif untuk mencari petak sawah yang paling produktif
def produktif():
    counter_p = 0
    dict_pro = {}
    while counter_p < counter:
        data_dict = petak_sawah[counter_p]
        lokasi = data_dict['Lokasi']
        hari = data_dict['Hari Panen']
        berat = data_dict['Berat Gabah']

        while hari+data_dict['Hari Panen'] < 365:
            berat = berat + data_dict['Berat Gabah']
            hari = hari + data_dict['Hari Panen']

        counter_p += 1
        if lokasi not in dict_pro:
            dict_pro[lokasi] = berat

        elif lokasi in dict_pro:    
            berat2 = dict_pro[lokasi] + berat
            dict_pro[lokasi] = berat2
            
    tertinggi = max(dict_pro, key=dict_pro.get)
    print('Terproduktif :',tertinggi,'Dengan Total Gabah sebanyak:', dict_pro[tertinggi],'Ton')

(layerR, layerG, layerB) = img.split()
layerRn = np.array(layerR)
layerGn = np.array(layerG)
layerBn = np.array(layerB)

rowlayer = layerR.size[0]
collayer = layerR.size[1]

layerRn = layerRn.reshape(rowlayer*collayer,1)
layerGn = layerGn.reshape(rowlayer*collayer,1)
layerBn = layerBn.reshape(rowlayer*collayer,1)
datalayer = np.column_stack((layerRn,layerGn,layerBn))

namafile = "Fileteks Python.txt"
test = baca_data(namafile)
print('=====================Dictionary===========================================================')
print('Dictionary',petak_sawah,'\n')
print('=====================List Petak Sawah=====================================================')
print_data(test)
print('=====================Total Gabah dan Penjualan Selama Setahun=============================')
report()
produktif()
print('=====================Rata-Rata============================================================')
rerata_input = input('Lokasi yang ingin dicari rata-ratanya(Case Sensitive) : ')
print('Rerata', rerata_input, 'adalah',rerata(rerata_input))
