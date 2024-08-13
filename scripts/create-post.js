const copyButton = document.getElementById("copy");
copyButton.addEventListener("click", () => {
  const data = getFormData();
  const jsonData = JSON.stringify(data, null, 2);
  navigator.clipboard.writeText(jsonData);
});

// Function to get all inputs from the container
function getFormData() {
  const container = document.querySelector(".main-subcontainer");
  const formData = {};

  // Get selected difficulty
  const difficulty = container.querySelector(
    'input[name="difficulty"]:checked'
  );
  if (difficulty) {
    formData.difficulty = difficulty.value;
  }

  // Get selected variant
  const variant = container.querySelector('input[name="variant"]:checked');
  if (variant) {
    formData.variant = variant.value;
  }

  // Get genre
  const genre = container.querySelector("#genre");
  if (genre) {
    formData.genre = genre.value;
  }

  // Get all checked tags
  const tags = Array.from(
    container.querySelectorAll('.tags input[type="checkbox"]:checked')
  );
  formData.tags = tags.map((tag) => tag.id);

  // Get title
  const title = container.querySelector("#title");
  if (title) {
    formData.title = title.value;
  }

  // Get intro text
  const intro = container.querySelector("#intro");
  if (intro) {
    formData.intro = intro.value;
  }

  // Get rules text
  const rules = container.querySelector("#rules");
  if (rules) {
    formData.rules = rules.value;
  }

  return formData;
}
