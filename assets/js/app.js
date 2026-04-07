import { Application } from "/assets/js/lib/stimulus.js";
import { register_controllers } from '/assets/js/controllers/index.js'

window.Stimulus = Application.start();
register_controllers(Stimulus)
