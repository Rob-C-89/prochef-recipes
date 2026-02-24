const deleteCommentModalEl = document.getElementById("deleteCommentModal");
const deleteCommentConfirm = document.getElementById("deleteCommentConfirm");
const deleteRecipeModalEl = document.getElementById("deleteRecipeModal");
const deleteRecipeConfirm = document.getElementById("deleteRecipeConfirm");
const deleteRecipeButton = document.querySelector(".delete-recipe-btn");
const deleteCommentButtons = document.querySelectorAll(".delete-comment-btn");

if (deleteRecipeModalEl && deleteRecipeConfirm && deleteRecipeButton) {
  const deleteRecipeModal = new bootstrap.Modal(deleteRecipeModalEl);
  deleteRecipeButton.addEventListener("click", (e) => {
    const deleteUrl = e.currentTarget.getAttribute("data-delete-url");
    deleteRecipeConfirm.href = deleteUrl || "#";
    deleteRecipeModal.show();
  });
}

if (deleteCommentModalEl && deleteCommentConfirm && deleteCommentButtons.length) {
  const deleteCommentModal = new bootstrap.Modal(deleteCommentModalEl);
  deleteCommentButtons.forEach((button) => {
    button.addEventListener("click", (e) => {
      const deleteUrl = e.currentTarget.getAttribute("data-delete-url");
      deleteCommentConfirm.href = deleteUrl || "#";
      deleteCommentModal.show();
    });
  });
}