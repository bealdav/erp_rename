# erp_rename
rename odoo modules


# Examples
erp_rename.py "oldname1:new1,old2:new2"

show this output:

UPDATE ir_model_data SET module = 'old2' WHERE module = 'new2';

UPDATE ir_module_module SET name = 'old2' WHERE name = 'new2';

UPDATE ir_module_module_dependency SET name = 'old2' WHERE name = 'new2';

UPDATE ir_model_data SET module = 'oldname1' WHERE module = 'new1';

UPDATE ir_module_module SET name = 'oldname1' WHERE name = 'new1';

UPDATE ir_module_module_dependency SET name = 'oldname1' WHERE name = 'new1';
