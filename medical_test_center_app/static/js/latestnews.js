// Set the API endpoint for the latest articles
const apiEndpoint = "https://gnews.io/api/v4/search?q=Médecine&lang=fr&country=fr&max=10&apikey=ce16040df07ac247cb8a30d2ca7e3682";

document.addEventListener("DOMContentLoaded", function () {
  // Fetch data from the API
  fetch(apiEndpoint)
    .then(response => response.json())
    .then(data => {
      // Log the data to the console
      console.log("Fetched data:", data);

      // Get the news container element
      const newsContainer = document.getElementById('news-container');

      // Create an array to store the articles
      const articles = data.articles || [];

      // Loop through each article and create HTML elements
      articles.forEach(article => {
        // Create a new div element for each article
        const articleDiv = document.createElement('div');
        articleDiv.className = 'news-mySlides';

        // Create a new div element for the news content
        const newsContentDiv = document.createElement('div');
        newsContentDiv.className = 'news-content';

        // Create a new anchor element for the title
        const titleLink = document.createElement('a');
        titleLink.href = article.url;
        titleLink.textContent = article.title;

        // Create a new paragraph element for the description
        const descriptionParagraph = document.createElement('p');
        descriptionParagraph.textContent = article.description;

        // Append title and description to news content div
        newsContentDiv.appendChild(titleLink);
        newsContentDiv.appendChild(descriptionParagraph);

        // Append news content to article div
        articleDiv.appendChild(newsContentDiv);

        // Append the article div to the news container
        newsContainer.appendChild(articleDiv);
      });

      // After adding all articles, initialize the slideshow
      initNewsSlideshow(articles.length);
    })
    .catch(error => {
      // Log any errors to the console
      console.error("Error fetching data:", error);
    });
});

// Function to initialize the news slideshow
function initNewsSlideshow(totalSlides) {
  let newsIndex = 0;
  showNewsSlides(newsIndex);

  // Set interval to change news slide every 8 seconds
  setInterval(() => {
    newsIndex++;
    if (newsIndex >= totalSlides) {
      newsIndex = 0;
    }
    showNewsSlides(newsIndex);
  }, 8000);

  // Add event listener for the "Previous" button
  const prevButton = document.getElementById('prev-button');
  prevButton.addEventListener('click', () => {
    newsIndex--;
    if (newsIndex < 0) {
      newsIndex = totalSlides - 1;
    }
    showNewsSlides(newsIndex);
  });

  // Add event listener for the "Next" button
  const nextButton = document.getElementById('next-button');
  nextButton.addEventListener('click', () => {
    newsIndex++;
    if (newsIndex >= totalSlides) {
      newsIndex = 0;
    }
    showNewsSlides(newsIndex);
  });
}

// Function to display the current news slide
function showNewsSlides(index) {
  const newsSlides = document.getElementsByClassName('news-mySlides');
  for (let i = 0; i < newsSlides.length; i++) {
    newsSlides[i].style.display = 'none';
  }
  newsSlides[index].style.display = 'block';
}
