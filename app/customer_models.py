from  .models import create_databaseConnection






def update_customerDetails(customer_id, first_name, last_name, email, phone, gender, state):
    query = """
        UPDATE customers
        SET first_name = %s,
            last_name = %s,
            state_address = %s,
            email_address = %s,
            phone_number = %s,
            gender = %s
        WHERE customer_id = %s
    """
    values = (first_name, last_name, state, email, phone, gender, customer_id)

    try:
        database_connection = create_databaseConnection()
        if database_connection is not None:
            cursor = database_connection.cursor()
            cursor.execute(query, values)
            database_connection.commit()
            if cursor.rowcount > 0:
                print("Customer details successfully updated for ID:", customer_id)
            else:
                print("No customer found with ID:", customer_id)
    except Error as e:
        print(f"Database error occurred: {e}")
        if database_connection:
            database_connection.rollback()
    finally:
        if cursor:
            cursor.close()
        if database_connection:
            database_connection.close()




def update_tour_bookings(tour_id, customer_id):
    query = "UPDATE tour_bookings SET tour_id = %s WHERE customer_id = %s"
    database_connection = None
    cursor = None

    try:
        database_connection = create_databaseConnection()
        cursor = database_connection.cursor()
        cursor.execute(query, (tour_id, customer_id))
        database_connection.commit()
        if cursor.rowcount > 0:
            print(f"Successfully updated tour_id for customer_id {customer_id}")
            return True
        else:
            print(f"No record found to update for customer_id {customer_id}")
            return False
    except Exception as e:
        logging.error(f"Error in update_tour_bookings: {e}")
        if database_connection:
            database_connection.rollback()
        return False
    finally:
        if cursor:
            cursor.close()
        if database_connection:
            database_connection.close()






def fetch_customer_details(customer_id):
    query = """SELECT
                c.customer_id,
                c.first_name, 
                c.last_name,
                c.state_address,
                c.email_address,
                c.phone_number
              FROM
                customers c
              WHERE c.customer_id = %s;"""  # Assuming you're using a placeholder for a parameterized query

    try:
        database_connection = create_databaseConnection()
        cursor = database_connection.cursor()
        cursor.execute(query, (customer_id,))  # Pass customer_id as a tuple
        customer_data = cursor.fetchall()  # Fetch all rows returned by the query
        return customer_data
    except Exception as e:
        print(f"Database error occurred: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if database_connection:
            database_connection.close()





def fetch_customer_email(customer_id):
    query="""SELECT
                c.email_address
              FROM
                customers c

             WHERE c.customer_id = %s;"""
    try:
        database_connection=create_databaseConnection()
        cursor=database_connection.cursor()
        cursor.execute(query, (customer_id,))
        customer_data=cursor.fetchall()

        return customer_data[0][0]

    except Exception as e:
        print(f"Database error occurred: {e}")
        return None

    finally:
        if cursor:
            cursor.close()
        if database_connection:
            database_connection.close()

  



def update_customer_email(customer_email,customer_id):
    query = "UPDATE customers SET email_address = %s WHERE customer_id = %s"
    database_connection = None
    cursor = None
    try:
        database_connection = create_databaseConnection()
        cursor = database_connection.cursor()
        cursor.execute(query,(customer_email, customer_id))
        database_connection.commit()
        if cursor.rowcount > 0:
            return True
        else:
            return False

    except Exception as e:
        logging.error(f"Error in update_tour_bookings: {e}")
        if database_connection:
            database_connection.rollback()
        return False
    finally:
        if cursor:
            cursor.close()
        if database_connection:
            database_connection.close()







def fetch_customer_name(customer_id):
    query= """SELECT
                c.first_name, 
                c.last_name
              FROM
                customers c
              WHERE c.customer_id = %s;""" 

    database_connection = None
    cursor = None

    try:
        database_connection=create_databaseConnection()
        cursor=database_connection.cursor()
        cursor.execute(query, (customer_id,))
        customer_data=cursor.fetchall()
        return customer_data[0]

    except Exception as e:
        print(f"Database error occurred: {e}")
        return None

    finally:
        if cursor:
            cursor.close()
        if database_connection:
            database_connection.close()







def update_customer_name(first_name, last_name,customer_id):
    query = "UPDATE customers SET first_name = %s, last_name = %s WHERE customer_id = %s"
    database_connection = None
    cursor = None
    try:
        database_connection=create_databaseConnection()
        cursor=database_connection.cursor()
        cursor.execute(query, (first_name,last_name))
        database_connection.commit()
        if cursor.rowcount > 0:
            return True
        else:
            return False

    except Exception as e:
        logging.error(f"Error in update_tour_bookings: {e}")
        if database_connection:
            database_connection.rollback()
        return False
    finally:
        if cursor:
            cursor.close()
        if database_connection:
            database_connection.close()



   






# print(fetch_customer_name(1))

















