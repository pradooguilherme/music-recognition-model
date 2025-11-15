#  Modelo para Classificação de Gêneros Musicais em Espectrogramas  

O projeto tem como objetivo **identificar, a partir de uma imagem, se uma música pertence ao gênero eletrônico ou clássico**.  

---

### Transformando áudio em imagem  

Para representar o áudio visualmente, foram utilizados **espectrogramas**, que mostram como as frequências de uma música variam ao longo do tempo.  

Essas imagens foram geradas por meio da **Transformada de Fourier de Curto Termo (STFT)**, que permite analisar a distribuição das frequências em pequenos intervalos de tempo.  

Com essa abordagem, utilizei a biblioteca **yt_dlp** para baixar trechos de 15 segundos de músicas de cada gênero, garantindo material suficiente para análise. A conversão do áudio em espectrogramas foi realizada com a biblioteca **Librosa**, especializada em análise de áudio.  

---

###  Treinamento do modelo  

Com os espectrogramas prontos, utilizei a biblioteca **FastAI** para o treinamento, escolhendo o modelo **ResNet18**, pré-treinado para reconhecimento de imagens. O treinamento foi realizado na plataforma **Kaggle**, aproveitando seus recursos de computação em nuvem.  

O dataset foi composto por **20 imagens de espectrogramas de músicas eletrônicas** e **20 de músicas clássicas**.  

Durante o treinamento, o conjunto de dados foi dividido em:  
-  **Training set:** usado para que o modelo aprenda os padrões das imagens;  
-  **Validation set:** usado para testar previsões e ajustar parâmetros ao longo das épocas.  

---

###  Resultados  

Após **5 épocas de treinamento**, o modelo obteve uma **taxa de erro de 12,5%**.  
Em testes com imagens externas, alcançou **83% de acurácia**, comprovando sua capacidade de generalização.  

---

###  Conclusão e próximos passos  

O bom desempenho do modelo, mesmo com um dataset pequeno, está relacionado ao uso de uma **ResNet18 pré-treinada**, que aproveita conhecimento prévio de reconhecimento de imagens.  

 **Possíveis melhorias futuras:**  
- Aumentar o tempo dos trechos musicais para capturar mais variações sonoras;  
- Realizar mais épocas de treinamento para refinar os padrões de classificação.  

---

### 🧰 Tecnologias utilizadas  

-  **Python**  
-  **FastAI**  
-  **Librosa**  
-  **yt_dlp**  
-  **Kaggle**  
-  **Hugging Face**

🔗 [Demo no Hugging Face](https://huggingface.co/spaces/pradooguilherme/music-recognition-model)
