window.onload = function(){
    document.getElementById("loading-gif").style.display = "none";

    poem = {
        init:function(){
            document.getElementById("submit-btn").addEventListener("click", this.getPoem)
        },
    
        getPoem:function(event){
            document.getElementById("loading-gif").style.display = "block";
            dropdownMenu = document.getElementById("id_author_name")
            authorName = dropdownMenu.options[dropdownMenu.selectedIndex].text

            promise = ajax.getData('/get-poem/', authorName)
            
            promise.then(data => {
                poemElement = document.getElementById("poem")

                poemElement.innerHTML = ''
                poemElement.style.display = "flex"

                var h1 = document.createElement('h1')

                h1.innerText = data.text[0].title

                poemElement.append(h1)

                var div = document.createElement('div')

                data.text[0].lines.forEach((x, i) => {
                    var p = document.createElement('p')
                    p.innerHTML = x
                    div.append(p)
                })

                poemElement.append(div)
                document.getElementById("loading-gif").style.display = "none";
            })
        }, 

        
    }

    ajax = {
        getData:function(url, data){
            return fetch(url, {
                method: "POST",
                headers: {
                    "X-CSRFToken": cookie.getCookie('csrftoken'),
                },
                body: JSON.stringify({
                    myData: data
                })
            }).then(function (response) {
                return response.json();
            })
            .then(function (data) {
                return data
            })
            .catch(function (err) {
                console.log(err);
            })
        }
    }

    cookie = {
        getCookie:function(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
    }

    poem.init()
}




