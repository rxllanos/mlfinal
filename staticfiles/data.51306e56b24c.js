document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#Inventario').style.display = 'none';
    document.querySelector('#Pendientes').style.display = 'none';
    document.querySelectorAll('button').forEach(button => {button.onclick = function() {
            showPage(this.dataset.page);
        }
    });
});

function showPage(page) {
    document.querySelector('#Pendientes').style.display = 'none';
    document.querySelector('#Inventario').style.display = 'none';

    if(page === 'Pendientes') {
      document.querySelector('#Pendientes').style.display = 'block';
      fPendientes();
      }
    if(page === 'Inventario') {
      document.querySelector('#Inventario').style.display = 'block';
      finventario();
      }  

}

function finventario(){
}


function fPendientes(){
    document.querySelector('#Pendientes').style.display = 'none';
    document.querySelector('#Pendientes').style.display = 'block';
    // document.querySelector('#task_list').innerHTML =''; 
    fetch('/tasks/task-list/')
    .then(response => response.json())
    .then(data => {
      data.forEach(item => {
                const task_entry = document.createElement('div');
                task_entry.className = 'task_entry';
                task_entry.innerHTML += ` Categoria: ${item.group_set}, Nombre: ${item.title}, Completado : ${item.completado}. `;
                var btn = document.createElement("BUTTON");
                btn.setAttribute = ("class", "negative ui button");   
                btn.class = "negative ui button"; 
                btn.innerHTML = "Borrar";   
                btn.className = "del";
                btn.value = item.id;               
                task_entry.appendChild(btn);
                var btn1 = document.createElement("BUTTON");
                btn1.setAttribute = ("class", "negative ui button");  
                btn1.class = "negative ui button";  
                btn1.value = item.id;  
                btn1.dataset.section = item.tcompletado; 
                if(item.tcompletado==true){
                btn1.innerHTML = "No completado?";
                }
                else {
                btn1.innerHTML = "Terminado?";
                }   
                btn1.className = "comp";
                if (item.tcompletado) {
                btn1.dataset.section1 = false 
                } else {
                btn1.dataset.section1 = true
                }          
                task_entry.appendChild(btn1);    
                task_entry.innerHTML += "<hr>";
                if (item.tcompletado) {
                    task_entry.style.textDecorationLine = "line-through";
                } 
                else {
                task_entry.style.backgroundColor = "#FDFEFE";
                }
                document.querySelector('#task_list').append(task_entry);  
        })
    })
    .catch(error => {
        console.log('Error:', error);
    });
}

document.addEventListener('click', event => {
    var csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const element = event.target;
    if (element.className === 'del') {
      fetch(`tasks/task-delete/${element.value}/`, {
        method: 'DELETE',
        headers: {
              'Content-Type':'application/json',
              'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
        })
      }) 
      .then(
        setTimeout(function() {
          window.location.reload();
        }, 3000)
      );   
    }
    
    if (element.className === 'comp') {
        fetch(`tasks/task-update/${element.value}/`, {
          method: 'PUT',
          headers: {
                'Content-Type':'application/json',
                'X-CSRFToken': csrf_token,
          },
          body: JSON.stringify({
            tcompletado : element.dataset.section1,
          })
        }) 
        .then(
          setTimeout(function() {
            window.location.reload();
          }, 3000)
        );   
    } 
})