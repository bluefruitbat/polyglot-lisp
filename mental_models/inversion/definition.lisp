;; Inversion Mental Model
;; Specific Lisp definition file

(defpackage :inversion
  (:use :cl)
  (:export :apply-inversion))

(in-package :inversion)

(defun apply-inversion (goal)
  "Invert the problem: instead of achieving the goal, avoid the failure modes."
  (format t "~%=== Inversion Mental Model ===~%")
  (format t "Goal: ~a~%" goal)
  (format t "What would cause failure?~%")
  (format t "Avoid those paths to succeed.~%~%")
  (list :avoid-failure goal))

;; End of definition
