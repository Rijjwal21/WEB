
data.forEach((element, i) => {
    const main = document.querySelector(".cardContainer")
    const card = document.createElement('div');
    card.classList = 'card';
    const movieCard = `
    <img src="${data[i].image}" alt="Document Image">
                <div class="info">
                    <h2>${data[i].title}</h2>
                    <span>${data[i].date}</span>
    `;
    
    card.innerHTML += movieCard;
    main.appendChild(card);
});
const area = document.querySelectorAll(".card img");
console.log(area);

document.querySelectorAll(".card img").forEach( image =>{
    image.onClick = () => {
        prompt("Helo")
        document.querySelector('.popup-image').style.display = 'block';
        document.querySelector('.pop-image img').src = image.getAttribute('src');   
     }
});