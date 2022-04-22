function insta_link(){
    var insta_href = document.getElementById("instagram")
    var insta = document.getElementById("instagram");
    var insta_alterado = insta.href.slice(38);

    var url = "https://instagram.com/"+insta_alterado;
    insta_href.setAttribute("href", url)
    //alert("Link: " +  insta_href);
}