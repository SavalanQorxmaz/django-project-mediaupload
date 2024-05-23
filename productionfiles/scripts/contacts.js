
const contactsIcon = document.getElementById('contacts-icon')
const contacts = document.getElementById('contacts')





    // if(contacts.classList.contains('contacts-show'))
 contactsIcon.addEventListener('click',(e)=>{
    e.preventDefault()
    if(contacts.classList.contains('contacts-show')&& e.target.classList.contains('contacts-icon-close')){
        contacts.classList.remove('contacts-show')
        contacts.classList.add('contacts-hide')
        e.target.classList.remove('contacts-icon-close')
        e.target.classList.add('contacts-icon-open')
        contactsIcon.innerHTML = ' &#9742;'
        document.body.style.overflow = 'auto'
    }
    else {
    
        contacts.classList.remove('contacts-hide')
        contacts.classList.add('contacts-show') 
        e.target.classList.add('contacts-icon-close')
        e.target.classList.remove('contacts-icon-open')
        contactsIcon.innerHTML = '&#x2718;'

        document.body.style.overflow = 'hidden'
    }
 
 }  )

