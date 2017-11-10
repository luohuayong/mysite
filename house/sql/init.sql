-- 产权
INSERT INTO house_chanquan (name) VALUES ('40年');
INSERT INTO house_chanquan (name) VALUES ('50年');
INSERT INTO house_chanquan (name) VALUES ('70年');

-- 朝向
INSERT INTO house_chaoxiang (name) VALUES ('东');
INSERT INTO house_chaoxiang (name) VALUES ('南');
INSERT INTO house_chaoxiang (name) VALUES ('西');
INSERT INTO house_chaoxiang (name) VALUES ('北');
INSERT INTO house_chaoxiang (name) VALUES ('东南');
INSERT INTO house_chaoxiang (name) VALUES ('西南');
INSERT INTO house_chaoxiang (name) VALUES ('西北');
INSERT INTO house_chaoxiang (name) VALUES ('东北');
INSERT INTO house_chaoxiang (name) VALUES ('南北');
INSERT INTO house_chaoxiang (name) VALUES ('东西');

-- 建筑类型
INSERT INTO house_jianzhu (name) VALUES ('塔楼');
INSERT INTO house_jianzhu (name) VALUES ('板楼');
INSERT INTO house_jianzhu (name) VALUES ('板塔结合');
INSERT INTO house_jianzhu (name) VALUES ('联排');
INSERT INTO house_jianzhu (name) VALUES ('叠拼');
INSERT INTO house_jianzhu (name) VALUES ('双拼');
INSERT INTO house_jianzhu (name) VALUES ('独栋');

-- 楼层
INSERT INTO house_louceng (name,lou,min,max) VALUES ('低层/多层','低层',0,8);
INSERT INTO house_louceng (name,lou,min,max) VALUES ('中层/多层','中层',0,8);
INSERT INTO house_louceng (name,lou,min,max) VALUES ('高层/多层','高层',0,8);
INSERT INTO house_louceng (name,lou,min,max) VALUES ('低层/小高层','低层',8,18);
INSERT INTO house_louceng (name,lou,min,max) VALUES ('中层/小高层','中层',8,18);
INSERT INTO house_louceng (name,lou,min,max) VALUES ('高层/小高层','高层',8,18);
INSERT INTO house_louceng (name,lou,min,max) VALUES ('低层/高层','低层',18,33);
INSERT INTO house_louceng (name,lou,min,max) VALUES ('中层/高层','中层',18,33);
INSERT INTO house_louceng (name,lou,min,max) VALUES ('高层/高层','高层',18,33);
INSERT INTO house_louceng (name,lou,min,max) VALUES ('低层/超高层','低层',33,100);
INSERT INTO house_louceng (name,lou,min,max) VALUES ('中层/超高层','中层',33,100);
INSERT INTO house_louceng (name,lou,min,max) VALUES ('高层/超高层','高层',33,100);

-- 户型
INSERT INTO house_huxing (name,shit,ting,wei) VALUES ('1室1厅1卫',1,1,1);
INSERT INTO house_huxing (name,shit,ting,wei) VALUES ('2室1厅1卫',2,1,1);
INSERT INTO house_huxing (name,shit,ting,wei) VALUES ('2室2厅1卫',2,2,1);
INSERT INTO house_huxing (name,shit,ting,wei) VALUES ('2室2厅2卫',2,2,2);
INSERT INTO house_huxing (name,shit,ting,wei) VALUES ('3室1厅1卫',3,1,1);
INSERT INTO house_huxing (name,shit,ting,wei) VALUES ('3室2厅1卫',3,2,1);
INSERT INTO house_huxing (name,shit,ting,wei) VALUES ('3室2厅2卫',3,2,2);
INSERT INTO house_huxing (name,shit,ting,wei) VALUES ('4室2厅1卫',4,2,1);
INSERT INTO house_huxing (name,shit,ting,wei) VALUES ('4室2厅2卫',4,2,2);
INSERT INTO house_huxing (name,shit,ting,wei) VALUES ('4室2厅3卫',4,2,3);
INSERT INTO house_huxing (name,shit,ting,wei) VALUES ('4室2厅4卫',4,2,4);
INSERT INTO house_huxing (name,shit,ting,wei) VALUES ('5室2厅2卫',5,2,2);
INSERT INTO house_huxing (name,shit,ting,wei) VALUES ('5室2厅3卫',5,2,3);
INSERT INTO house_huxing (name,shit,ting,wei) VALUES ('5室2厅4卫',5,2,4);
INSERT INTO house_huxing (name,shit,ting,wei) VALUES ('5室3厅3卫',5,3,3);

