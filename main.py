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
        self.idioma = 'eng' # Idioma que sera usado para leitura dos caracteres da imagem
    
    
    def filtroEliminaRuido(self, img):
        imgRed = cv2.resize(img, (self.larguraImg, self.alturaImg)) # Redimensionamento da imagem
        imgCinza = cv2.cvtColor(imgRed, cv2.COLOR_BGR2GRAY) # Conversão da imagem para escala de cinza
        imgBlur = cv2.GaussianBlur(imgCinza, (5, 5), 0) # Aplicação do filtro de borramento para eliminar ruídos na imagem
        return imgBlur
        
    def filtroBinarizaImgMetodo1(self, img):
        imgTresh = cv2.inRange(img, 110, 220) # Binarização da imagem
        return imgTresh
    
    def filtroBinarizaImgMetodo2(self, img):
        imgTresh = cv2.inRange(img, 120, 220) # Binarização da imagem
        return imgTresh
     
        
    '''
        Função que irá fazer a leitura dos caracteres da imagem
    '''
    def leituraOCR(self, img):
        texto = pytesseract.image_to_string(img, lang=self.idioma) # Leitura dos caracteres da imagem no idioma inglês
        return texto
    
    def main(self):
        #try:
        for i in sorted(glob.glob(self.caminhoDataset)): 
            imagem = cv2.imread(i)   # Leitura da imagem da base dados
              
            imagemSemRuido = self.filtroEliminaRuido(imagem)
            imagemBin = self.filtroBinarizaImgMetodo1(imagemSemRuido)
            imagemRegiaoCPF = imagemBin[211:251, 370:545]
            
            CPF = self.leituraOCR(imagemRegiaoCPF)
            tamanhoTexto = len(CPF)
            
            if tamanhoTexto > 10:
                print(CPF)
                print(tamanhoTexto)
            else:
                CPF = self.leituraOCR(imagemRegiaoCPF)
            
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