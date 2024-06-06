const submitIdeaButton = document.getElementById('submit-idea');

submitIdeaButton.addEventListener('click', () => {
  const ideaTitle = prompt('Enter your business idea title:');
  const ideaDescription = prompt('Enter your business idea description:');
  const ideaIndustry = prompt('Enter your business idea industry:');
  const ideaInvestmentPotential = prompt('Enter your business idea investment potential:');

  const idea = {
    title: ideaTitle,
    description: ideaDescription,
    industry: ideaIndustry,
    investmentPotential: ideaInvestmentPotential,
  };

  fetch('/api/business_ideas', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(idea),
  })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
});
