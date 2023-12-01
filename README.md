# Fragments of an infinite field

“Fragments of an infinite field” is a compositional system in which an idealized plant species is generated and arranged in a potentially infinite field of foliage. The main environmental parameter of the composition is the determination of a season of the year. The season determines the landscape’s colors and defines specific phenomena for each of them, such as rain in summer, snow in winter, petals falling in autumn, and pollen in spring. The flower has several possible variables, which can be macro aspects, affecting the entire population of the species, or micro, affecting each individual of the species differently. For example, the number of petals can be equal in all individuals or not. The number of filaments and other structures of the flower can undergo minor deviations, generating small mutations. The confusion between the figure (plant) and the background (earth, sky, other natural elements) is fascinating from a compositional point of view. The background colors are, most of the time, colors present in the figures, often breaking the boundary between them and, therefore, generating chromatic masses. In this project I also intend to research the following question: How to create parameters that resemble a living organism's growth? In this sense, the project approaches digital morphogenesis and the development of procedural organisms.

[Art Blocks • curated collection • series 4](https://www.artblocks.io/collections/curated/projects/0xa7d8d9ef8d8ce8992df33d8b8cf4aebabd5bd270/159)

[In Conversation with Monica Rizzolli](https://beta.cent.co/artblocks/+6xptyk)

[As the NFT Market Explodes Again, Artists Fend Off Old Art-World Power Structures](https://time.com/6106679/nft-art-rise/)

[Monica Rizzolli: conheça a artista programadora que contribui na mudança de paradigmas dos NFTs no mundo da arte](https://vogue.globo.com/lifestyle/cultura/noticia/2021/12/monica-rizzolli-conheca-artista-programadora-que-contribui-na-mudanca-de-paradigmas-dos-nfts-no-mundo-da-arte.html)

[Mestres do algoritmo: computadores vão tomar lugar de artistas?](https://veja.abril.com.br/cultura/mestres-do-algoritmo-computadores-vao-tomar-lugar-de-artistas/)

## How to generate the images

This is a generative work, and it pseudo-randomness is originated by a seed. This seed is a string of 64 hexadecimal characters, referred in the code as `hash`. The same hash will always generate the same image. In order to generate an image, just follow the steps below. Please notice these instructions are very generic, and you may need to adapt them to your specific environment. The author of this work opted to not provide instructions using specific tools, because tools are not universal and may become obsolete in the future.

1. Install, setup and run a web server. You may use any web server, as you will only need to serve simple static pages;
2. Clone this repository to your web server's root directory (or any other directory you may want to use):
```
git clone https://github.com/Morfologia-digital/fragmentsOfAnInfiniteField.git
```
3. You are already able to access the images in your browser. Simply access it using the URL of your web server. For example, if you are running the web server locally, you may access the images using the URL `http://localhost/fragmentsOfAnInfiniteField/`, However, the images will be generated with the default hash. 

4. If you want to generate images with a specific hash, you will need to edit the `sketh.js` file. Simply change the value of the variable `hash` to the desired hash. This code is located at the very top of the file (lines 1 to 4):
```
tokenData = {
  hash: "0x0a17a93f55859d66b31e0d78685737ef365fa3edf49fa887090059a157e2d9c8",
  tokenId: "159000091",
};
```

5. The code currently is fulfilling the web browser inner dimensions. If you want to generate images with a specific size, you will need to edit the `sketh.js` file. Simply change the value of the `TDIM` variable to the desired values. This variables is also located at the very top of the file (line 8):
```
var TDIM = Math.min(window.innerWidth, window.innerHeight);
```
Replace `Math.min(window.innerWidth, window.innerHeight)` with the desired values. For example, to generate a 1000x1000 image, you may use:
```
var TDIM = 1000;
```
Please note that once this work is drawn using a HTML canvas, the image will be rasterized. Therefore, it is not possible to generate images with infinite resolution. The maximum resolution is limited by the size of the canvas. Also, the maximum since of the canvas is limited by your web browser. Please check your web browser documentation for more information.