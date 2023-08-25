function like_post(id){
    console.log("function is called");
    let like_heart = document.getElementById(`like-heart-${id}`);

    console.log(like_heart.className);
    if(like_heart.classList.contains("far")){
        console.log("true function is called");
        fetch(`/like/${id}`, {
            method: 'PUT',
            body: JSON.stringify({
                like: true
            })
        }).then((response) => {
            response.json()
        }).then((data) => {
            console.log(data)
            document.location.reload()
        })
    }
    else{
        console.log("false function is called");
        fetch(`/like/${id}`, {
            method: 'PUT',
            body: JSON.stringify({
                like: false
            })
        }).then((response) => {
            response.json()
        }).then((data) => {
            document.location.reload()
            console.log(data)
        })
    }
}


document.addEventListener("DOMContentLoaded", function (event) {
    
    // adding search bar input
    let searchbar_icon = document.querySelector("#searchbar_icon");

    const searchbar = document.createElement('input');
    searchbar.className = "form-control"
    searchbar.type = "text";
    searchbar.id = "searchbar_input"

    searchbar_icon.addEventListener('click', ()=> {
        searchbar_icon.classList.toggle("activate");

        const searchbar_box = document.getElementById("searchbar_box");

        if(searchbar_icon.classList.contains("activate")){
            searchbar_box.appendChild(searchbar);
            searchbar.focus();
        }
        else{
            searchbar_box.removeChild(searchbar);
            console.log("searchbar removed");
        }
        
    });

    // Toggle sidebar
    let headerToggler = document.getElementById('header-toggler');
    let sidebar = document.getElementById('side-bar');
    let bodyPage= document.getElementById('body-page');
    let header = document.getElementById('header');
    let categoriesText = document.querySelector('.sidebar_logo');
    
    if(headerToggler && sidebar && bodyPage && header){
        headerToggler.addEventListener('click', () => {

            // show sidebar
            sidebar.classList.toggle('show');

            //change icon
            headerToggler.classList.toggle('fa-times');

            //add padding to body
            bodyPage.classList.toggle('body_page')

            //add padding to header
            header.classList.toggle('body_page');

            categoriesText.classList.toggle('hide-inner');
        })
    }
    
    
});

