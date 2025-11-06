# Modelo para classificação de genêros musicais em espectogramas

O projeto tem como objetivo **identificar, a partir de uma imagem, se uma música é do estilo eletrônico ou clássico**.
---

## Transformando áudio em imagem

Para representar o áudio visualmente, escolhi os **espectrogramas**, que mostram como as frequências de uma música variam ao longo do tempo.  
Para gerá-los, utilizei a **Transformada de Fourier de Curto Termo (STFT)**, que permite analisar a distribuição das frequências ao longo do tempo.  

Com essa abordagem em mente, utilizei a biblioteca **yt_dlp** para baixar trechos de 15 segundos de músicas de cada gênero, garantindo material suficiente para a análise.  
A conversão do áudio em espectrogramas foi realizada com a biblioteca **Librosa**, especializada em análise de áudio.    

---

## Treinamento

Com os espectrogramas prontos, utilizei a biblioteca **FastAI** para o treinamento, escolhendo o modelo **ResNet18**, pré-treinado para reconhecimento de imagens.  
O treinamento foi realizado na plataforma **Kaggle**, aproveitando seus recursos de computação em nuvem.

O dataset foi composto por **20 imagens de espectrogramas de músicas eletrônicas** e **20 imagens de músicas clássicas**.  

Durante o treinamento, o dataset foi dividido em dois conjuntos:  
- **Training set:** para que o modelo aprenda os padrões das imagens;  
- **Validation set:** para testar previsões e ajustar parâmetros ao longo das épocas.
  
---

## Resultados  

Após 5 épocas de treinamento, o modelo obteve uma **taxa de erro de 12,5%**.  
Ao testá-lo com imagens externas, alcançou uma **taxa de acerto de 83% em 12 imagens**, comprovando sua capacidade de generalização.  

---

## 🚀 Conclusão  

O bom desempenho do modelo, mesmo com um dataset pequeno, está ligado ao uso de uma **ResNet18 pré-treinada**, que permite aproveitar conhecimento prévio em reconhecimento de imagens.  

Próximos passos:

  - Aumentar o tempo dos trechos musicais para capturar mais variações sonoras;  
  - Treinar o modelo por mais épocas, permitindo um refinamento mais profundo dos padrões de classificação.  

---

## 💡 Tecnologias utilizadas  

- **Python**  
- **FastAI**  
- **Librosa**  
- **yt_dlp**  
- **Kaggle**  
- **Hugging Face**  

---

🔗 [Demo no Hugging Face](https://huggingface.co/spaces/pradooguilherme/music-recognition-model)
