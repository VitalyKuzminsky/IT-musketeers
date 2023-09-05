import pymysql
from itm import settings

def get_users_information():
    conn = pymysql.connect(host=settings.DATABASES.get('default').get('HOST'),
                           user=settings.DATABASES.get('default').get('USER'),
                           password=settings.DATABASES.get('default').get('PASSWORD'),
                           db=settings.DATABASES.get('default').get('NAME'),
                           port=int(settings.DATABASES.get('default').get('PORT')),
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)
    try:
        with conn.cursor() as cursor:
            response = f'''
            SELECT 
                `cu`.`id`, 
                `cu`.`username`, 
                `cu`.`first_name`, 
                `cu`.`last_name`, 
                `cu`.`is_staff`, 
                `cu`.`is_superuser`, 
                (SELECT GROUP_CONCAT(`bh`.`organization_holder`) FROM `mainapp_balanceholder` bh 
                WHERE `bh`.`id` IN (SELECT `ah`.`balanceholder_id` FROM `mainapp_customuser_available_holders` ah 
                                    WHERE `ah`.`customuser_id` = `cu`.`id`)) AS 'balanceholder_id' 
            FROM `mainapp_customuser` cu
            '''
            cursor.execute(response)
            response = cursor.fetchall()
    finally:
        conn.close()

    return response