const cardsPerPage = 5; 
let currentPage = 1;

function displayCards(pageNumber) {
    const cardContainer = document.getElementById('card-container');
    cardContainer.innerHTML = '';

    const startIndex = (pageNumber - 1) * cardsPerPage;
    const endIndex = startIndex + cardsPerPage;

    for (let i = startIndex; i < endIndex && i < cardsData.length; i++) {
        const card = cardsData[i];
        const cardElement = createCardElement(card);
        cardContainer.appendChild(cardElement);
    }
}

function createCardElement(card) {
    const cardElement = document.createElement('div');
    cardElement.className = 'card';

    const cardImage = document.createElement('img');
    cardImage.src = card.image_url; // Assuming 'image_url' is the property in your card data
    cardImage.className = 'card-img-top';
    cardImage.alt = card.title;

    const cardBody = document.createElement('div');
    cardBody.className = 'card-body';

    const cardTitle = document.createElement('span');
    cardTitle.className = 'card-title';
    cardTitle.textContent = card.title;

    const cardSubtitle1 = document.createElement('span');
    cardSubtitle1.className = 'card-text';
    cardSubtitle1.textContent = card.subtitle;

    const cardSubtitle2 = document.createElement('span');
    cardSubtitle2.className = 'card-text';
    cardSubtitle2.textContent = card.subtitle2;

    cardBody.appendChild(cardTitle);
    cardBody.appendChild(cardSubtitle1);
    cardBody.appendChild(cardSubtitle2);

    cardElement.appendChild(cardImage);
    cardElement.appendChild(cardBody);

    return cardElement;
}


function createPaginationLinks() {
    const totalPages = Math.ceil(cardsData.length / cardsPerPage);
    const paginationContainer = document.getElementById('pagination');
    paginationContainer.innerHTML = ''; 

    for (let i = 1; i <= totalPages; i++) {
        const pageLink = document.createElement('a');
        pageLink.href = '#'; 
        pageLink.textContent = i;

        pageLink.addEventListener('click', function () {
            currentPage = i;
            displayCards(currentPage);
        });

        paginationContainer.appendChild(pageLink);
    }
}

// Initial setup
displayCards(currentPage);
createPaginationLinks();
