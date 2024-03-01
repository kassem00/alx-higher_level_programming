;; Initialize package sources
(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/") t)
(package-initialize)

;; Ensure use-package is installed
(unless (package-installed-p 'use-package)
  (package-refresh-contents)
  (package-install 'use-package))

;; Require use-package
(eval-when-compile
  (require 'use-package))

;; Your existing configuration below this line
;; For example, setting up lsp-mode and ccls
(use-package lsp-mode
  :ensure t
  :commands (lsp lsp-deferred)
  :hook ((c-mode c++-mode objc-mode) . lsp-deferred))

(use-package ccls
  :ensure t
  :after projectile
  :hook ((c-mode c++-mode objc-mode cuda-mode) .
         (lambda () (require 'ccls) (lsp))))

(setq-default explicit-shell-file-name "/bin/zsh")
(setq-default shell-file-name "/bin/zsh")

'(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-enabled-themes '(cyberpunk))
 '(custom-safe-themes
   '("cae6181b05f4624308a41ec209db44bc3e00e8ee74cad3f1eebf5b13cc48d86a" default))
 '(default
    ((t
      (:family "DejaVu Sans Mono" :foundry "PfEd" :slant normal :weight bold :height 151 :width normal)))))

```Emacs
(setq c-default-style "bsd"
      c-basic-offset 8
      tab-width 8
      indent-tabs-mode t)
```

```Emacs
(require 'whitespace)
(setq whitespace-style '(face empty lines-tail trailing))
(global-whitespace-mode t)
```

```Emacs
(setq column-number-mode t)
(add-to-list 'custom-theme-load-path "~/.emacs.d/themes/")
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-faces-vector
   [default default default italic underline success warning error])
 '(ansi-color-names-vector
   ["black" "red3" "ForestGreen" "yellow3" "blue" "magenta3" "DeepSkyBlue" "gray50"])
 '(custom-enabled-themes '(cyberpunk))
 '(custom-safe-themes
   '("7b8f5bbdc7c316ee62f271acf6bcd0e0b8a272fdffe908f8c920b0ba34871d98" "871b064b53235facde040f6bdfa28d03d9f4b966d8ce28fb1725313731a2bcc8" "046a2b81d13afddae309930ef85d458c4f5d278a69448e5a5261a5c78598e012" "d445c7b530713eac282ecdeea07a8fa59692c83045bf84dd112dd738c7bcad1d" "90f9914dbbbe8f52d02e56244ff45b5472120d01f231c8c4d337bf1d6526d172" "7b36f45e5f014ac5d463fa1fe627df6f2094484d31c8aecd77d06b0b23844532" "7c6839d4288d6c25d4b47ee2bba67f27583a73761e8b098ae083647d2e1fa4fe" "1344adb76a35c7fa4a30340193941f848559f10094054dd08b89e9562157e80d" "6aae2eb39ce5d67379a4718cdb295b819c4100ddda8d07fa8eab53289a0b7551" "69181eaef039bcc5a89d03112d1ca47ccf63e79a0cae2b800dc2a7053996d2f7" "8e85902264a5baeda5e8fb86f5712bff6e5920fbdcaa196e139093aaacca34c2" "16913f11cf754c7d93349fc816c5d83eeb0a789a0004dd84b87ad769234cae59" "04d735f8b10046cbfc7a002f199cac24e3db78b2d19a5f6c8ea182493f3c0655" "b099685963c251fb3ed5dd60237bda3390a11372221dfc9d168aa54e7b1c252e" "8fcbb734e7e8bb240299fb3d52628f13e1af6dda931ced3e1df7a0eb41309608" "cae6181b05f4624308a41ec209db44bc3e00e8ee74cad3f1eebf5b13cc48d86a" default))
 '(default
    ((t
      (:family "DejaVu Sans Mono" :foundry "PfEd" :slant normal :weight bold :height 151 :width normal))))
 '(fci-rule-color "#383838")
 '(package-selected-packages '(## company-ebdb eglot nano-theme ggtags all company))
 '(set-cursor-color "#ffffff")
 '(setq-default cursor-type t))


(add-to-list 'default-frame-alist '(fullscreen . fullscreen))

;; Hide menu bar
(menu-bar-mode -1)

;; Hide tool bar
(tool-bar-mode -1)
(setq inhibit-startup-screen t)
(put 'scroll-left 'disabled nil)
