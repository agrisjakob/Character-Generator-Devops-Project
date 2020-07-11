cd /CI

ansible-playbook -i inventory --vault-password-file=/home/agrisjakob/ansiblep playbook.yaml
