import pickle
class load30xarxes(object):


    def __init__(self,ponderacio,de_facil_a_dificil):

        self.__ponderacio=ponderacio
        self.__de_facil_a_dificil=de_facil_a_dificil


        if self.__ponderacio==1 and self.__de_facil_a_dificil==0:

            x0 = pickle.load(open('../30xPonderacio1FacilDificil/x0.csv', 'rb'))
            x1 = pickle.load(open('../30xPonderacio1FacilDificil/x1.csv', 'rb'))
            x2 = pickle.load(open('../30xPonderacio1FacilDificil/x2.csv', 'rb'))
            x3 = pickle.load(open('../30xPonderacio1FacilDificil/x3.csv', 'rb'))
            x4 = pickle.load(open('../30xPonderacio1FacilDificil/x4.csv', 'rb'))
            x5 = pickle.load(open('../30xPonderacio1FacilDificil/x5.csv', 'rb'))
            x6 = pickle.load(open('../30xPonderacio1FacilDificil/x6.csv', 'rb'))
            x7 = pickle.load(open('../30xPonderacio1FacilDificil/x7.csv', 'rb'))
            x8 = pickle.load(open('../30xPonderacio1FacilDificil/x8.csv', 'rb'))
            x9 = pickle.load(open('../30xPonderacio1FacilDificil/x9.csv', 'rb'))
            x10 = pickle.load(open('../30xPonderacio1FacilDificil/x10.csv', 'rb'))
            x11 = pickle.load(open('../30xPonderacio1FacilDificil/x11.csv', 'rb'))
            x12 = pickle.load(open('../30xPonderacio1FacilDificil/x12.csv', 'rb'))
            x13 = pickle.load(open('../30xPonderacio1FacilDificil/x13.csv', 'rb'))
            x14 = pickle.load(open('../30xPonderacio1FacilDificil/x14.csv', 'rb'))
            x15 = pickle.load(open('../30xPonderacio1FacilDificil/x15.csv', 'rb'))
            x16 = pickle.load(open('../30xPonderacio1FacilDificil/x16.csv', 'rb'))
            x17 = pickle.load(open('../30xPonderacio1FacilDificil/x17.csv', 'rb'))
            x18 = pickle.load(open('../30xPonderacio1FacilDificil/x18.csv', 'rb'))
            x19 = pickle.load(open('../30xPonderacio1FacilDificil/x19.csv', 'rb'))
            x20 = pickle.load(open('../30xPonderacio1FacilDificil/x20.csv', 'rb'))
            x21 = pickle.load(open('../30xPonderacio1FacilDificil/x21.csv', 'rb'))
            x22 = pickle.load(open('../30xPonderacio1FacilDificil/x22.csv', 'rb'))
            x23 = pickle.load(open('../30xPonderacio1FacilDificil/x23.csv', 'rb'))
            x24 = pickle.load(open('../30xPonderacio1FacilDificil/x24.csv', 'rb'))
            x25 = pickle.load(open('../30xPonderacio1FacilDificil/x25.csv', 'rb'))
            x26 = pickle.load(open('../30xPonderacio1FacilDificil/x26.csv', 'rb'))
            x27 = pickle.load(open('../30xPonderacio1FacilDificil/x27.csv', 'rb'))
            x28 = pickle.load(open('../30xPonderacio1FacilDificil/x28.csv', 'rb'))
            x29 = pickle.load(open('../30xPonderacio1FacilDificil/x29.csv', 'rb'))


            self.__xarxa = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19,
                        x20, x21,x22, x23, x24, x25, x26, x27, x28, x29]

        if self.__ponderacio == 2 and self.__de_facil_a_dificil==0:
            x0 = pickle.load(open('../30xPonderacio2FacilDificil/x0.csv', 'rb'))
            x1 = pickle.load(open('../30xPonderacio2FacilDificil/x1.csv', 'rb'))
            x2 = pickle.load(open('../30xPonderacio2FacilDificil/x2.csv', 'rb'))
            x3 = pickle.load(open('../30xPonderacio2FacilDificil/x3.csv', 'rb'))
            x4 = pickle.load(open('../30xPonderacio2FacilDificil/x4.csv', 'rb'))
            x5 = pickle.load(open('../30xPonderacio2FacilDificil/x5.csv', 'rb'))
            x6 = pickle.load(open('../30xPonderacio2FacilDificil/x6.csv', 'rb'))
            x7 = pickle.load(open('../30xPonderacio2FacilDificil/x7.csv', 'rb'))
            x8 = pickle.load(open('../30xPonderacio2FacilDificil/x8.csv', 'rb'))
            x9 = pickle.load(open('../30xPonderacio2FacilDificil/x9.csv', 'rb'))
            x10 = pickle.load(open('../30xPonderacio2FacilDificil/x10.csv', 'rb'))
            x11 = pickle.load(open('../30xPonderacio2FacilDificil/x11.csv', 'rb'))
            x12 = pickle.load(open('../30xPonderacio2FacilDificil/x12.csv', 'rb'))
            x13 = pickle.load(open('../30xPonderacio2FacilDificil/x13.csv', 'rb'))
            x14 = pickle.load(open('../30xPonderacio2FacilDificil/x14.csv', 'rb'))
            x15 = pickle.load(open('../30xPonderacio2FacilDificil/x15.csv', 'rb'))
            x16 = pickle.load(open('../30xPonderacio2FacilDificil/x16.csv', 'rb'))
            x17 = pickle.load(open('../30xPonderacio2FacilDificil/x17.csv', 'rb'))
            x18 = pickle.load(open('../30xPonderacio2FacilDificil/x18.csv', 'rb'))
            x19 = pickle.load(open('../30xPonderacio2FacilDificil/x19.csv', 'rb'))
            x20 = pickle.load(open('../30xPonderacio2FacilDificil/x20.csv', 'rb'))
            x21 = pickle.load(open('../30xPonderacio2FacilDificil/x21.csv', 'rb'))
            x22 = pickle.load(open('../30xPonderacio2FacilDificil/x22.csv', 'rb'))
            x23 = pickle.load(open('../30xPonderacio2FacilDificil/x23.csv', 'rb'))
            x24 = pickle.load(open('../30xPonderacio2FacilDificil/x24.csv', 'rb'))
            x25 = pickle.load(open('../30xPonderacio2FacilDificil/x25.csv', 'rb'))
            x26 = pickle.load(open('../30xPonderacio2FacilDificil/x26.csv', 'rb'))
            x27 = pickle.load(open('../30xPonderacio2FacilDificil/x27.csv', 'rb'))
            x28 = pickle.load(open('../30xPonderacio2FacilDificil/x28.csv', 'rb'))
            x29 = pickle.load(open('../30xPonderacio2FacilDificil/x29.csv', 'rb'))

            self.__xarxa = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19,
                            x20, x21, x22, x23, x24, x25, x26, x27, x28, x29]

        if self.__ponderacio == 3 and self.__de_facil_a_dificil==0:
            x0 = pickle.load(open('../30xPonderacio3FacilDificil/x0.csv', 'rb'))
            x1 = pickle.load(open('../30xPonderacio3FacilDificil/x1.csv', 'rb'))
            x2 = pickle.load(open('../30xPonderacio3FacilDificil/x2.csv', 'rb'))
            x3 = pickle.load(open('../30xPonderacio3FacilDificil/x3.csv', 'rb'))
            x4 = pickle.load(open('../30xPonderacio3FacilDificil/x4.csv', 'rb'))
            x5 = pickle.load(open('../30xPonderacio3FacilDificil/x5.csv', 'rb'))
            x6 = pickle.load(open('../30xPonderacio3FacilDificil/x6.csv', 'rb'))
            x7 = pickle.load(open('../30xPonderacio3FacilDificil/x7.csv', 'rb'))
            x8 = pickle.load(open('../30xPonderacio3FacilDificil/x8.csv', 'rb'))
            x9 = pickle.load(open('../30xPonderacio3FacilDificil/x9.csv', 'rb'))
            x10 = pickle.load(open('../30xPonderacio3FacilDificil/x10.csv', 'rb'))
            x11 = pickle.load(open('../30xPonderacio3FacilDificil/x11.csv', 'rb'))
            x12 = pickle.load(open('../30xPonderacio3FacilDificil/x12.csv', 'rb'))
            x13 = pickle.load(open('../30xPonderacio3FacilDificil/x13.csv', 'rb'))
            x14 = pickle.load(open('../30xPonderacio3FacilDificil/x14.csv', 'rb'))
            x15 = pickle.load(open('../30xPonderacio3FacilDificil/x15.csv', 'rb'))
            x16 = pickle.load(open('../30xPonderacio3FacilDificil/x16.csv', 'rb'))
            x17 = pickle.load(open('../30xPonderacio3FacilDificil/x17.csv', 'rb'))
            x18 = pickle.load(open('../30xPonderacio3FacilDificil/x18.csv', 'rb'))
            x19 = pickle.load(open('../30xPonderacio3FacilDificil/x19.csv', 'rb'))
            x20 = pickle.load(open('../30xPonderacio3FacilDificil/x20.csv', 'rb'))
            x21 = pickle.load(open('../30xPonderacio3FacilDificil/x21.csv', 'rb'))
            x22 = pickle.load(open('../30xPonderacio3FacilDificil/x22.csv', 'rb'))
            x23 = pickle.load(open('../30xPonderacio3FacilDificil/x23.csv', 'rb'))
            x24 = pickle.load(open('../30xPonderacio3FacilDificil/x24.csv', 'rb'))
            x25 = pickle.load(open('../30xPonderacio3FacilDificil/x25.csv', 'rb'))
            x26 = pickle.load(open('../30xPonderacio3FacilDificil/x26.csv', 'rb'))
            x27 = pickle.load(open('../30xPonderacio3FacilDificil/x27.csv', 'rb'))
            x28 = pickle.load(open('../30xPonderacio3FacilDificil/x28.csv', 'rb'))
            x29 = pickle.load(open('../30xPonderacio3FacilDificil/x29.csv', 'rb'))

            self.__xarxa = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19,
                            x20, x21, x22, x23, x24, x25, x26, x27, x28, x29]

        if self.__ponderacio == 4 and self.__de_facil_a_dificil==0:
            x0 = pickle.load(open('../30xPonderacio4FacilDificil/x0.csv', 'rb'))
            x1 = pickle.load(open('../30xPonderacio4FacilDificil/x1.csv', 'rb'))
            x2 = pickle.load(open('../30xPonderacio4FacilDificil/x2.csv', 'rb'))
            x3 = pickle.load(open('../30xPonderacio4FacilDificil/x3.csv', 'rb'))
            x4 = pickle.load(open('../30xPonderacio4FacilDificil/x4.csv', 'rb'))
            x5 = pickle.load(open('../30xPonderacio4FacilDificil/x5.csv', 'rb'))
            x6 = pickle.load(open('../30xPonderacio4FacilDificil/x6.csv', 'rb'))
            x7 = pickle.load(open('../30xPonderacio4FacilDificil/x7.csv', 'rb'))
            x8 = pickle.load(open('../30xPonderacio4FacilDificil/x8.csv', 'rb'))
            x9 = pickle.load(open('../30xPonderacio4FacilDificil/x9.csv', 'rb'))
            x10 = pickle.load(open('../30xPonderacio4FacilDificil/x10.csv', 'rb'))
            x11 = pickle.load(open('../30xPonderacio4FacilDificil/x11.csv', 'rb'))
            x12 = pickle.load(open('../30xPonderacio4FacilDificil/x12.csv', 'rb'))
            x13 = pickle.load(open('../30xPonderacio4FacilDificil/x13.csv', 'rb'))
            x14 = pickle.load(open('../30xPonderacio4FacilDificil/x14.csv', 'rb'))
            x15 = pickle.load(open('../30xPonderacio4FacilDificil/x15.csv', 'rb'))
            x16 = pickle.load(open('../30xPonderacio4FacilDificil/x16.csv', 'rb'))
            x17 = pickle.load(open('../30xPonderacio4FacilDificil/x17.csv', 'rb'))
            x18 = pickle.load(open('../30xPonderacio4FacilDificil/x18.csv', 'rb'))
            x19 = pickle.load(open('../30xPonderacio4FacilDificil/x19.csv', 'rb'))
            x20 = pickle.load(open('../30xPonderacio4FacilDificil/x20.csv', 'rb'))
            x21 = pickle.load(open('../30xPonderacio4FacilDificil/x21.csv', 'rb'))
            x22 = pickle.load(open('../30xPonderacio4FacilDificil/x22.csv', 'rb'))
            x23 = pickle.load(open('../30xPonderacio4FacilDificil/x23.csv', 'rb'))
            x24 = pickle.load(open('../30xPonderacio4FacilDificil/x24.csv', 'rb'))
            x25 = pickle.load(open('../30xPonderacio4FacilDificil/x25.csv', 'rb'))
            x26 = pickle.load(open('../30xPonderacio4FacilDificil/x26.csv', 'rb'))
            x27 = pickle.load(open('../30xPonderacio4FacilDificil/x27.csv', 'rb'))
            x28 = pickle.load(open('../30xPonderacio4FacilDificil/x28.csv', 'rb'))
            x29 = pickle.load(open('../30xPonderacio4FacilDificil/x29.csv', 'rb'))

            self.__xarxa = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19,
                        x20, x21, x22, x23, x24, x25, x26, x27, x28, x29]

        if self.__ponderacio == 5 and self.__de_facil_a_dificil==0:
            x0 = pickle.load(open('../30xPonderacio5FacilDificil/x0.csv', 'rb'))
            x1 = pickle.load(open('../30xPonderacio5FacilDificil/x1.csv', 'rb'))
            x2 = pickle.load(open('../30xPonderacio5FacilDificil/x2.csv', 'rb'))
            x3 = pickle.load(open('../30xPonderacio5FacilDificil/x3.csv', 'rb'))
            x4 = pickle.load(open('../30xPonderacio5FacilDificil/x4.csv', 'rb'))
            x5 = pickle.load(open('../30xPonderacio5FacilDificil/x5.csv', 'rb'))
            x6 = pickle.load(open('../30xPonderacio5FacilDificil/x6.csv', 'rb'))
            x7 = pickle.load(open('../30xPonderacio5FacilDificil/x7.csv', 'rb'))
            x8 = pickle.load(open('../30xPonderacio5FacilDificil/x8.csv', 'rb'))
            x9 = pickle.load(open('../30xPonderacio5FacilDificil/x9.csv', 'rb'))
            x10 = pickle.load(open('../30xPonderacio5FacilDificil/x10.csv', 'rb'))
            x11 = pickle.load(open('../30xPonderacio5FacilDificil/x11.csv', 'rb'))
            x12 = pickle.load(open('../30xPonderacio5FacilDificil/x12.csv', 'rb'))
            x13 = pickle.load(open('../30xPonderacio5FacilDificil/x13.csv', 'rb'))
            x14 = pickle.load(open('../30xPonderacio5FacilDificil/x14.csv', 'rb'))
            x15 = pickle.load(open('../30xPonderacio5FacilDificil/x15.csv', 'rb'))
            x16 = pickle.load(open('../30xPonderacio5FacilDificil/x16.csv', 'rb'))
            x17 = pickle.load(open('../30xPonderacio5FacilDificil/x17.csv', 'rb'))
            x18 = pickle.load(open('../30xPonderacio5FacilDificil/x18.csv', 'rb'))
            x19 = pickle.load(open('../30xPonderacio5FacilDificil/x19.csv', 'rb'))
            x20 = pickle.load(open('../30xPonderacio5FacilDificil/x20.csv', 'rb'))
            x21 = pickle.load(open('../30xPonderacio5FacilDificil/x21.csv', 'rb'))
            x22 = pickle.load(open('../30xPonderacio5FacilDificil/x22.csv', 'rb'))
            x23 = pickle.load(open('../30xPonderacio5FacilDificil/x23.csv', 'rb'))
            x24 = pickle.load(open('../30xPonderacio5FacilDificil/x24.csv', 'rb'))
            x25 = pickle.load(open('../30xPonderacio5FacilDificil/x25.csv', 'rb'))
            x26 = pickle.load(open('../30xPonderacio5FacilDificil/x26.csv', 'rb'))
            x27 = pickle.load(open('../30xPonderacio5FacilDificil/x27.csv', 'rb'))
            x28 = pickle.load(open('../30xPonderacio5FacilDificil/x28.csv', 'rb'))
            x29 = pickle.load(open('../30xPonderacio5FacilDificil/x29.csv', 'rb'))

            self.__xarxa = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19,
                        x20, x21, x22, x23, x24, x25, x26, x27, x28, x29]



        if self.__ponderacio == 1 and self.__de_facil_a_dificil == 1:
                x0 = pickle.load(open('../30xPonderacio1DificilFacil/x0.csv', 'rb'))
                x1 = pickle.load(open('../30xPonderacio1DificilFacil/x1.csv', 'rb'))
                x2 = pickle.load(open('../30xPonderacio1DificilFacil/x2.csv', 'rb'))
                x3 = pickle.load(open('../30xPonderacio1DificilFacil/x3.csv', 'rb'))
                x4 = pickle.load(open('../30xPonderacio1DificilFacil/x4.csv', 'rb'))
                x5 = pickle.load(open('../30xPonderacio1DificilFacil/x5.csv', 'rb'))
                x6 = pickle.load(open('../30xPonderacio1DificilFacil/x6.csv', 'rb'))
                x7 = pickle.load(open('../30xPonderacio1DificilFacil/x7.csv', 'rb'))
                x8 = pickle.load(open('../30xPonderacio1DificilFacil/x8.csv', 'rb'))
                x9 = pickle.load(open('../30xPonderacio1DificilFacil/x9.csv', 'rb'))
                x10 = pickle.load(open('../30xPonderacio1DificilFacil/x10.csv', 'rb'))
                x11 = pickle.load(open('../30xPonderacio1DificilFacil/x11.csv', 'rb'))
                x12 = pickle.load(open('../30xPonderacio1DificilFacil/x12.csv', 'rb'))
                x13 = pickle.load(open('../30xPonderacio1DificilFacil/x13.csv', 'rb'))
                x14 = pickle.load(open('../30xPonderacio1DificilFacil/x14.csv', 'rb'))
                x15 = pickle.load(open('../30xPonderacio1DificilFacil/x15.csv', 'rb'))
                x16 = pickle.load(open('../30xPonderacio1DificilFacil/x16.csv', 'rb'))
                x17 = pickle.load(open('../30xPonderacio1DificilFacil/x17.csv', 'rb'))
                x18 = pickle.load(open('../30xPonderacio1DificilFacil/x18.csv', 'rb'))
                x19 = pickle.load(open('../30xPonderacio1DificilFacil/x19.csv', 'rb'))
                x20 = pickle.load(open('../30xPonderacio1DificilFacil/x20.csv', 'rb'))
                x21 = pickle.load(open('../30xPonderacio1DificilFacil/x21.csv', 'rb'))
                x22 = pickle.load(open('../30xPonderacio1DificilFacil/x22.csv', 'rb'))
                x23 = pickle.load(open('../30xPonderacio1DificilFacil/x23.csv', 'rb'))
                x24 = pickle.load(open('../30xPonderacio1DificilFacil/x24.csv', 'rb'))
                x25 = pickle.load(open('../30xPonderacio1DificilFacil/x25.csv', 'rb'))
                x26 = pickle.load(open('../30xPonderacio1DificilFacil/x26.csv', 'rb'))
                x27 = pickle.load(open('../30xPonderacio1DificilFacil/x27.csv', 'rb'))
                x28 = pickle.load(open('../30xPonderacio1DificilFacil/x28.csv', 'rb'))
                x29 = pickle.load(open('../30xPonderacio1DificilFacil/x29.csv', 'rb'))

                self.__xarxa = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18,
                                x19,x20, x21, x22, x23, x24, x25, x26, x27, x28, x29]

        if self.__ponderacio == 2 and self.__de_facil_a_dificil == 1:
                x0 = pickle.load(open('../30xPonderacio2DificilFacil/x0.csv', 'rb'))
                x1 = pickle.load(open('../30xPonderacio2DificilFacil/x1.csv', 'rb'))
                x2 = pickle.load(open('../30xPonderacio2DificilFacil/x2.csv', 'rb'))
                x3 = pickle.load(open('../30xPonderacio2DificilFacil/x3.csv', 'rb'))
                x4 = pickle.load(open('../30xPonderacio2DificilFacil/x4.csv', 'rb'))
                x5 = pickle.load(open('../30xPonderacio2DificilFacil/x5.csv', 'rb'))
                x6 = pickle.load(open('../30xPonderacio2DificilFacil/x6.csv', 'rb'))
                x7 = pickle.load(open('../30xPonderacio2DificilFacil/x7.csv', 'rb'))
                x8 = pickle.load(open('../30xPonderacio2DificilFacil/x8.csv', 'rb'))
                x9 = pickle.load(open('../30xPonderacio2DificilFacil/x9.csv', 'rb'))
                x10 = pickle.load(open('../30xPonderacio2DificilFacil/x10.csv', 'rb'))
                x11 = pickle.load(open('../30xPonderacio2DificilFacil/x11.csv', 'rb'))
                x12 = pickle.load(open('../30xPonderacio2DificilFacil/x12.csv', 'rb'))
                x13 = pickle.load(open('../30xPonderacio2DificilFacil/x13.csv', 'rb'))
                x14 = pickle.load(open('../30xPonderacio2DificilFacil/x14.csv', 'rb'))
                x15 = pickle.load(open('../30xPonderacio2DificilFacil/x15.csv', 'rb'))
                x16 = pickle.load(open('../30xPonderacio2DificilFacil/x16.csv', 'rb'))
                x17 = pickle.load(open('../30xPonderacio2DificilFacil/x17.csv', 'rb'))
                x18 = pickle.load(open('../30xPonderacio2DificilFacil/x18.csv', 'rb'))
                x19 = pickle.load(open('../30xPonderacio2DificilFacil/x19.csv', 'rb'))
                x20 = pickle.load(open('../30xPonderacio2DificilFacil/x20.csv', 'rb'))
                x21 = pickle.load(open('../30xPonderacio2DificilFacil/x21.csv', 'rb'))
                x22 = pickle.load(open('../30xPonderacio2DificilFacil/x22.csv', 'rb'))
                x23 = pickle.load(open('../30xPonderacio2DificilFacil/x23.csv', 'rb'))
                x24 = pickle.load(open('../30xPonderacio2DificilFacil/x24.csv', 'rb'))
                x25 = pickle.load(open('../30xPonderacio2DificilFacil/x25.csv', 'rb'))
                x26 = pickle.load(open('../30xPonderacio2DificilFacil/x26.csv', 'rb'))
                x27 = pickle.load(open('../30xPonderacio2DificilFacil/x27.csv', 'rb'))
                x28 = pickle.load(open('../30xPonderacio2DificilFacil/x28.csv', 'rb'))
                x29 = pickle.load(open('../30xPonderacio2DificilFacil/x29.csv', 'rb'))

                self.__xarxa = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18,
                                x19,
                                x20, x21, x22, x23, x24, x25, x26, x27, x28, x29]

        if self.__ponderacio == 3 and self.__de_facil_a_dificil == 1:
                x0 = pickle.load(open('../30xPonderacio3DificilFacil/x0.csv', 'rb'))
                x1 = pickle.load(open('../30xPonderacio3DificilFacil/x1.csv', 'rb'))
                x2 = pickle.load(open('../30xPonderacio3DificilFacil/x2.csv', 'rb'))
                x3 = pickle.load(open('../30xPonderacio3DificilFacil/x3.csv', 'rb'))
                x4 = pickle.load(open('../30xPonderacio3DificilFacil/x4.csv', 'rb'))
                x5 = pickle.load(open('../30xPonderacio3DificilFacil/x5.csv', 'rb'))
                x6 = pickle.load(open('../30xPonderacio3DificilFacil/x6.csv', 'rb'))
                x7 = pickle.load(open('../30xPonderacio3DificilFacil/x7.csv', 'rb'))
                x8 = pickle.load(open('../30xPonderacio3DificilFacil/x8.csv', 'rb'))
                x9 = pickle.load(open('../30xPonderacio3DificilFacil/x9.csv', 'rb'))
                x10 = pickle.load(open('../30xPonderacio3DificilFacil/x10.csv', 'rb'))
                x11 = pickle.load(open('../30xPonderacio3DificilFacil/x11.csv', 'rb'))
                x12 = pickle.load(open('../30xPonderacio3DificilFacil/x12.csv', 'rb'))
                x13 = pickle.load(open('../30xPonderacio3DificilFacil/x13.csv', 'rb'))
                x14 = pickle.load(open('../30xPonderacio3DificilFacil/x14.csv', 'rb'))
                x15 = pickle.load(open('../30xPonderacio3DificilFacil/x15.csv', 'rb'))
                x16 = pickle.load(open('../30xPonderacio3DificilFacil/x16.csv', 'rb'))
                x17 = pickle.load(open('../30xPonderacio3DificilFacil/x17.csv', 'rb'))
                x18 = pickle.load(open('../30xPonderacio3DificilFacil/x18.csv', 'rb'))
                x19 = pickle.load(open('../30xPonderacio3DificilFacil/x19.csv', 'rb'))
                x20 = pickle.load(open('../30xPonderacio3DificilFacil/x20.csv', 'rb'))
                x21 = pickle.load(open('../30xPonderacio3DificilFacil/x21.csv', 'rb'))
                x22 = pickle.load(open('../30xPonderacio3DificilFacil/x22.csv', 'rb'))
                x23 = pickle.load(open('../30xPonderacio3DificilFacil/x23.csv', 'rb'))
                x24 = pickle.load(open('../30xPonderacio3DificilFacil/x24.csv', 'rb'))
                x25 = pickle.load(open('../30xPonderacio3DificilFacil/x25.csv', 'rb'))
                x26 = pickle.load(open('../30xPonderacio3DificilFacil/x26.csv', 'rb'))
                x27 = pickle.load(open('../30xPonderacio3DificilFacil/x27.csv', 'rb'))
                x28 = pickle.load(open('../30xPonderacio3DificilFacil/x28.csv', 'rb'))
                x29 = pickle.load(open('../30xPonderacio3DificilFacil/x29.csv', 'rb'))

                self.__xarxa = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18,
                                x19,x20, x21, x22, x23, x24, x25, x26, x27, x28, x29]

        if self.__ponderacio == 4 and self.__de_facil_a_dificil == 1:
                x0 = pickle.load(open('../30xPonderacio4DificilFacil/x0.csv', 'rb'))
                x1 = pickle.load(open('../30xPonderacio4DificilFacil/x1.csv', 'rb'))
                x2 = pickle.load(open('../30xPonderacio4DificilFacil/x2.csv', 'rb'))
                x3 = pickle.load(open('../30xPonderacio4DificilFacil/x3.csv', 'rb'))
                x4 = pickle.load(open('../30xPonderacio4DificilFacil/x4.csv', 'rb'))
                x5 = pickle.load(open('../30xPonderacio4DificilFacil/x5.csv', 'rb'))
                x6 = pickle.load(open('../30xPonderacio4DificilFacil/x6.csv', 'rb'))
                x7 = pickle.load(open('../30xPonderacio4DificilFacil/x7.csv', 'rb'))
                x8 = pickle.load(open('../30xPonderacio4DificilFacil/x8.csv', 'rb'))
                x9 = pickle.load(open('../30xPonderacio4DificilFacil/x9.csv', 'rb'))
                x10 = pickle.load(open('../30xPonderacio4DificilFacil/x10.csv', 'rb'))
                x11 = pickle.load(open('../30xPonderacio4DificilFacil/x11.csv', 'rb'))
                x12 = pickle.load(open('../30xPonderacio4DificilFacil/x12.csv', 'rb'))
                x13 = pickle.load(open('../30xPonderacio4DificilFacil/x13.csv', 'rb'))
                x14 = pickle.load(open('../30xPonderacio4DificilFacil/x14.csv', 'rb'))
                x15 = pickle.load(open('../30xPonderacio4DificilFacil/x15.csv', 'rb'))
                x16 = pickle.load(open('../30xPonderacio4DificilFacil/x16.csv', 'rb'))
                x17 = pickle.load(open('../30xPonderacio4DificilFacil/x17.csv', 'rb'))
                x18 = pickle.load(open('../30xPonderacio4DificilFacil/x18.csv', 'rb'))
                x19 = pickle.load(open('../30xPonderacio4DificilFacil/x19.csv', 'rb'))
                x20 = pickle.load(open('../30xPonderacio4DificilFacil/x20.csv', 'rb'))
                x21 = pickle.load(open('../30xPonderacio4DificilFacil/x21.csv', 'rb'))
                x22 = pickle.load(open('../30xPonderacio4DificilFacil/x22.csv', 'rb'))
                x23 = pickle.load(open('../30xPonderacio4DificilFacil/x23.csv', 'rb'))
                x24 = pickle.load(open('../30xPonderacio4DificilFacil/x24.csv', 'rb'))
                x25 = pickle.load(open('../30xPonderacio4DificilFacil/x25.csv', 'rb'))
                x26 = pickle.load(open('../30xPonderacio4DificilFacil/x26.csv', 'rb'))
                x27 = pickle.load(open('../30xPonderacio4DificilFacil/x27.csv', 'rb'))
                x28 = pickle.load(open('../30xPonderacio4DificilFacil/x28.csv', 'rb'))
                x29 = pickle.load(open('../30xPonderacio4DificilFacil/x29.csv', 'rb'))

                self.__xarxa = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19,
                                x20, x21, x22, x23, x24, x25, x26, x27, x28, x29]


        if self.__ponderacio == 5 and self.__de_facil_a_dificil == 1:
                x0 = pickle.load(open('../30xPonderacio5DificilFacil/x0.csv', 'rb'))
                x1 = pickle.load(open('../30xPonderacio5DificilFacil/x1.csv', 'rb'))
                x2 = pickle.load(open('../30xPonderacio5DificilFacil/x2.csv', 'rb'))
                x3 = pickle.load(open('../30xPonderacio5DificilFacil/x3.csv', 'rb'))
                x4 = pickle.load(open('../30xPonderacio5DificilFacil/x4.csv', 'rb'))
                x5 = pickle.load(open('../30xPonderacio5DificilFacil/x5.csv', 'rb'))
                x6 = pickle.load(open('../30xPonderacio5DificilFacil/x6.csv', 'rb'))
                x7 = pickle.load(open('../30xPonderacio5DificilFacil/x7.csv', 'rb'))
                x8 = pickle.load(open('../30xPonderacio5DificilFacil/x8.csv', 'rb'))
                x9 = pickle.load(open('../30xPonderacio5DificilFacil/x9.csv', 'rb'))
                x10 = pickle.load(open('../30xPonderacio5DificilFacil/x10.csv', 'rb'))
                x11 = pickle.load(open('../30xPonderacio5DificilFacil/x11.csv', 'rb'))
                x12 = pickle.load(open('../30xPonderacio5DificilFacil/x12.csv', 'rb'))
                x13 = pickle.load(open('../30xPonderacio5DificilFacil/x13.csv', 'rb'))
                x14 = pickle.load(open('../30xPonderacio5DificilFacil/x14.csv', 'rb'))
                x15 = pickle.load(open('../30xPonderacio5DificilFacil/x15.csv', 'rb'))
                x16 = pickle.load(open('../30xPonderacio5DificilFacil/x16.csv', 'rb'))
                x17 = pickle.load(open('../30xPonderacio5DificilFacil/x17.csv', 'rb'))
                x18 = pickle.load(open('../30xPonderacio5DificilFacil/x18.csv', 'rb'))
                x19 = pickle.load(open('../30xPonderacio5DificilFacil/x19.csv', 'rb'))
                x20 = pickle.load(open('../30xPonderacio5DificilFacil/x20.csv', 'rb'))
                x21 = pickle.load(open('../30xPonderacio5DificilFacil/x21.csv', 'rb'))
                x22 = pickle.load(open('../30xPonderacio5DificilFacil/x22.csv', 'rb'))
                x23 = pickle.load(open('../30xPonderacio5DificilFacil/x23.csv', 'rb'))
                x24 = pickle.load(open('../30xPonderacio5DificilFacil/x24.csv', 'rb'))
                x25 = pickle.load(open('../30xPonderacio5DificilFacil/x25.csv', 'rb'))
                x26 = pickle.load(open('../30xPonderacio5DificilFacil/x26.csv', 'rb'))
                x27 = pickle.load(open('../30xPonderacio5DificilFacil/x27.csv', 'rb'))
                x28 = pickle.load(open('../30xPonderacio5DificilFacil/x28.csv', 'rb'))
                x29 = pickle.load(open('../30xPonderacio5DificilFacil/x29.csv', 'rb'))

                self.__xarxa = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19,
                                x20, x21, x22, x23, x24, x25, x26, x27, x28, x29]

    def xarxa(self):
        return self.__xarxa


    def ponderacio(self):
        return self.__ponderacio


    def de_facil_a_dificil(self):
        return self.__de_facil_a_dificil

    def xarxa_cotxe_n(self,numero):
        return self.__xarxa[numero]
