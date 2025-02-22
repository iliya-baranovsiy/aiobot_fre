from random import randint

list_ = ["datas/roffles/00.jpg", "roffles/11.jpg",
         "datas/roffles/22.jpg",
         "datas/roffles/33.jpg",
         "datas/roffles/44.jpg",
         "datas/roffles/55.jpg",
         "datas/roffles/66.jpg",
         "datas/roffles/77.jpg",
         "datas/roffles/88.jpg",
         "datas/roffles/99.jpg",
         "datas/roffles/111.jpg",
         "datas/roffles/123.jpg",
         "datas/roffles/photo_5384133804010103440_y.jpg",
         "datas/roffles/photo_5384292425742280119_y.jpg",
         "datas/roffles/photo_5393592142334646688_x.jpg",
         "datas/roffles/photo_5395502032686800619_y.jpg",
         "datas/roffles/photo_5429105130961235594_x.jpg",
         "datas/roffles/photo_5454352567929791159_x.jpg",
         "datas/roffles/vid_1.mp4",
         "datas/roffles/canva.png",
         "datas/roffles/hz.png",
         "datas/roffles/func.png",
         "datas/roffles/djordj.jpg",
         "datas/roffles/rir.jpg",
         "datas/roffles/ser.png",
         "datas/roffles/photo_5454352567929791008_y.jpg", ]


def random_roffles():
    rand = randint(0, 25)
    return list_[rand]
