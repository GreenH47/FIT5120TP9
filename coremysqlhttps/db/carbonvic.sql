use test;
CREATE TABLE bill (
   id INT AUTO_INCREMENT PRIMARY KEY,
   subarea VARCHAR(100),
   electricity FLOAT,
   gas FLOAT,
   carbon FLOAT
);

INSERT INTO bill (subarea, electricity, gas, carbon)
VALUES
   ('Subarea 1', 50.2, 25.5, 10.1),
   ('Subarea 2', 40.1, 20.3, 8.2),
   ('Subarea 3', 35.7, 18.9, 7.5);

select * from bill;



INSERT INTO bill (subarea, electricity, gas, carbon) VALUES
('Lysterfield South', 786.75, 4833.33, 639.55),
('Doveton and Eumemmerring', 310.58, 3416.67, 356.57),
('Endeavour Hills', 361.50, 5083.33, 491.37),
('Hallam', 326.75, 4166.67, 414.61),
('Narre Warren North', 670.75, 6416.67, 703.67),
('Narre Warren and Narre Warren South', 349.67, 4666.67, 458.02),
('Berwick and Harkaway', 370.67, 4750.00, 471.94),
('Beaconsfield', 477.58, 4250.00, 479.03),
('Pearcedale', 480.08, 3833.33, 451.25),
('Lynbrook and Lyndhurst', 322.50, 4500.00, 435.95),
('Hampton Park', 298.67, 3833.33, 380.68),
('Botanic Ridge, Cannons Creek, Cranbourne', 346.33, 3833.33, 399.22),
('Clyde and Clyde North', 284.00, 3666.67, 363.48),
('Blind Bight, Tooradin and Warneet', 626.75, 6416.67, 686.56);