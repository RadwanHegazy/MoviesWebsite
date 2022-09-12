document.querySelectorAll('#search').forEach(item =>{
    item.addEventListener('click',function(){
        document.querySelector('.search').classList.toggle('view')
    })
})

document.querySelectorAll('#type').forEach(item =>{
    item.addEventListener('click',function(){
        document.querySelector('.type').classList.toggle('view')
    })
})
