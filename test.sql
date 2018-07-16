SELECT   CASE category 
            WHEN '法律咨询' THEN 1
            WHEN '房屋交易' THEN 12
            WHEN '二手市场' THEN 11
            WHEN '商品买卖' THEN 10
            WHEN '生活服务' THEN 9
            WHEN '招聘求职' THEN 8 
            WHEN '吃货天地' THEN 7
            WHEN '千岛万象' THEN 6
            WHEN '旅游专题' THEN 5
            WHEN '同城活动' THEN 4
            WHEN '龙友知道' THEN 3
            WHEN '全民记者' THEN 2
            WHEN '二手车市场' THEN 13
        ELSE 1 END 
FROM   content1  
LIMIT 1,10;

	
-- dede_archives
INSERT INTO `dede_archives` (
    `id`, `typeid2`, `sortrank`, `flag`, `ismake`, `channel`, `arcrank`, `click`, `money`, `title`, 
    `shorttitle`, `color`, `writer`, `source`, `litpic`, `pubdate`, `senddate`, `mid`, `keywords`, `lastpost`, 
    `scores`, `goodpost`, `badpost`, `voteid`, `notpost`, `description`, `filename`, `dutyadmin`, `tackid`, 
    `mtype`, `weight`, `typeid`) 
SELECT cast(str_id as signed) as `id`,  
        '0',1531454126, '', 1, 1, 0, 120, 0,
        title,
        '', '', 'admin', '菲龙网','', 1531454126, 1531453937, 1,
        keywords,
        1531454370, 2, 1, 0, 0, 0, title, '', 1, 0, 0, 0,
        CASE category 
            WHEN '法律咨询' THEN 1
            WHEN '房屋交易' THEN 12
            WHEN '二手市场' THEN 11
            WHEN '商品买卖' THEN 10
            WHEN '生活服务' THEN 9
            WHEN '招聘求职' THEN 8 
            WHEN '吃货天地' THEN 7
            WHEN '千岛万象' THEN 6
            WHEN '旅游专题' THEN 5
            WHEN '同城活动' THEN 4
            WHEN '龙友知道' THEN 3
            WHEN '全民记者' THEN 2
            WHEN '二手车市场' THEN 13
        ELSE 1 END as `typeid`
FROM   content1  
LIMIT 1,10;

-- VALUES
-- (1, 1 , 1531454126, '', 1, 1, 0, 120, 0, '标题', '', '', 'admin', '菲龙网', '', 1531454126, 1531453937, 1, '关键字', 1531454370, 2, 1, 0, 0, 0, '文章摘要', '', 1, 0, 0, 0, '0',),
-- (2, 12, '0', 1531560751, '', 1, 1, 0, 153, 0, '房屋交易', '', '', 'admin', '未知', '', 1531560751, 1531458233, 1, '房屋交易', 0, 0, 0, 0, 0, 0, '房屋交易', '', 1, 0, 0, 1),
-- (3, 12, '0', 3063259878, '', 1, 1, 0, 2, 0, '标题111', '', '', 'admin', '菲龙网', '', 1531560678, 1531458233, 1, '关键字', 0, 0, 0, 0, 0, 0, '文章摘要', '', 1, 0, 0, 1);
-- dede_addonarticle

INSERT INTO `dede_addonarticle` (`aid`, `typeid`, `body`) 
SELECT  cast(str_id as signed) as `aid` , CASE category 
            WHEN '法律咨询' THEN 1
            WHEN '房屋交易' THEN 12
            WHEN '二手市场' THEN 11
            WHEN '商品买卖' THEN 10
            WHEN '生活服务' THEN 9
            WHEN '招聘求职' THEN 8 
            WHEN '吃货天地' THEN 7
            WHEN '千岛万象' THEN 6
            WHEN '旅游专题' THEN 5
            WHEN '同城活动' THEN 4
            WHEN '龙友知道' THEN 3
            WHEN '全民记者' THEN 2
            WHEN '二手车市场' THEN 13
        ELSE 1 END  as `typeid`,
        content as `body` 
FROM   content1  
LIMIT 1,10;
-- VALUES
-- (1, 1, '<strong>内容页</strong>', '', '', '180.232.85.26'),
-- (2, 12, '房屋交易', '', '', '118.193.135.25'),
-- (3, 12, '<strong>内容页</strong>', '', '', '118.193.135.25');
-- dede_arctiny
INSERT INTO `dede_arctiny` (`id`, `typeid`, `typeid2`, `arcrank`, `channel`, `senddate`, `sortrank`, `mid`) 
SELECT  cast(str_id as signed) as `id` , CASE category 
            WHEN '法律咨询' THEN 1
            WHEN '房屋交易' THEN 12
            WHEN '二手市场' THEN 11
            WHEN '商品买卖' THEN 10
            WHEN '生活服务' THEN 9
            WHEN '招聘求职' THEN 8 
            WHEN '吃货天地' THEN 7
            WHEN '千岛万象' THEN 6
            WHEN '旅游专题' THEN 5
            WHEN '同城活动' THEN 4
            WHEN '龙友知道' THEN 3
            WHEN '全民记者' THEN 2
            WHEN '二手车市场' THEN 13
        ELSE 1 END  as `typeid`,
        '0', 0, 1, 1531453937, 1531454126, 1
FROM   content1  
LIMIT 1,10;
-- VALUES
-- (1, 1, '0', 0, 1, 1531453937, 1531454126, 1),
-- (2, 12, '0', 0, 1, 1531458233, 1531560751, 1),
-- (3, 12, '0', 0, 1, 1531453937, 1531454126, 1);