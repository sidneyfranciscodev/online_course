import AuthController from "/assets/js/controllers/auth_controller.js"

export function register_controllers(application) {
    application.register("auth", AuthController)
}