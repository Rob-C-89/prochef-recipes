const deleteCommentModal = document.getElementById("deleteCommentModal");
const deleteCommentConfirm = document.getElementById("deleteCommentConfirm");
const deleteCommentButton = document.querySelectorAll(".delete-comment-btn");

const deleteRecipeModal = document.getElementById("deleteRecipeModal");
const deleteRecipeConfirm = document.getElementById("deleteRecipeConfirm");
const deleteRecipeButton = document.querySelector(".delete-recipe-btn");

if (deleteRecipeModal && deleteRecipeConfirm && deleteRecipeButton) {
  const deleteRecipeModal = new bootstrap.Modal(deleteRecipeModal);
  deleteRecipeButton.addEventListener("click", (e) => {
    const deleteUrl = e.currentTarget.getAttribute("data-delete-url");
    deleteRecipeConfirm.href = deleteUrl || "#";
    deleteRecipeModal.show();
  });
}

if (deleteCommentModal && deleteCommentConfirm && deleteCommentButton.length) {
  const deleteCommentModal = new bootstrap.Modal(deleteCommentModal);
  deleteCommentButton.forEach((button) => {
    button.addEventListener("click", (e) => {
      const deleteUrl = e.currentTarget.getAttribute("data-delete-url");
      deleteCommentConfirm.href = deleteUrl || "#";
      deleteCommentModal.show();
    });
  });
}