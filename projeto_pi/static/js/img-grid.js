//Pega o elemento de cada imagem
var img_principal = document.getElementById("img_principal");

//Pega o caminho para cada imagem
var img_principal_src = document.getElementById("img_principal").src;


if (document.getElementById("img1")) {
    var img1 = document.getElementById("img1");
    var img1src = img1.src;
} 

if (document.getElementById("img2")) {
    var img2 = document.getElementById("img2");
    var img2src = img2.src;
} 

if (document.getElementById("img3")) {
    var img3 = document.getElementById("img3");
    var img3src = img3.src;
} 

//Funções para trocar a imagem principal pelas imagens selecionadas
img2.onmouseover = function(){
    img2.setAttribute("style", "border: 2px solid orange");
    img_principal.src = img2src;
}

img2.onmouseout = function(){
    img2.setAttribute("style", "border: none");
}

img3.onmouseover = function(){
    img3.setAttribute("style", "border: 2px solid orange");
    img_principal.src = img3src;
}

img3.onmouseout = function(){
    img3.setAttribute("style", "border: none");
}


img1.onmouseover = function() {
    img1.setAttribute("style", "border: 2px solid orange");
    img_principal.src = img1src;
}

img1.onmouseout = function(){
    img1.setAttribute("style", "border: none");
}
