function insta_link(){
    var insta_href = document.getElementById("instagram")
    var insta = document.getElementById("instagram").href;
    var insta_alterado = insta.search(insta.slice("@")+1);

    var url = "https://instagram.com/"+insta_alterado;
    insta_href.setAttribute("href", url)
    //alert("Link: " +  insta_href);
}