#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 20:48:24 2021

@author: estanislau
"""

import cv2
import glob
import pytesseract


class LeitorCPF():
    
    def __init__(self):
        self.caminhoDataset = '/home/estanislau/Projetos/LeitorCPF/dataset/*.jpg' # Caminho com as imagens das CNH's
        self.larguraImg = 731 # Largura padrão para redimensionar as imagens
        self.alturaImg = 495 # Altura padrão para redimensionar as imagens
    
    def filtros(self, img):
        imgRed = cv2.resize(img, (self.larguraImg, self.alturaImg)) # Redimensionamento da imagem
        imgCinza = cv2.cvtColor(imgRed, cv2.COLOR_BGR2GRAY) # Conversão da imagem para escala de cinza
        imgBlur = cv2.GaussianBlur(imgCinza, (5, 5), 0) # Aplicação do filtro de borramento para eliminar ruídos na imagem
        imgTresh = cv2.inRange(imgBlur, 112, 220) # Binarização da imagem
        return imgTresh
    
    def main(self):
        #try:
        for i in sorted(glob.glob(self.caminhoDataset)): 
            imagem = cv2.imread(i)   # Leitura da imagem da base dados
              
            imagemBin = self.filtros(imagem)
            imagemRegiaoCPF = imagemBin[211:251, 370:526]
            
            print(pytesseract.image_to_string(imagemRegiaoCPF, lang='eng'))
            
            cv2.imshow("Imagem", imagem)
            cv2.imshow("Imagem Bin", imagemBin)
            cv2.imshow("Imagem Reg", imagemRegiaoCPF)
            cv2.waitKey(0)
        #except:
        #    print("Erro no programa principal!")
        #finally:
        #   cv2.destroyAllWindows() 
        cv2.destroyAllWindows() 
        
    
if __name__ == '__main__':
    app = LeitorCPF()
    app.main()