import pre_process
import connect
import query_db
import query_doc
import find_tf_idf


def system_first_uploading():
    try:
        clean = pre_process.get_clean_data("https://en.wikipedia.org/wiki/Sport", "sport")
        text_arr = []

        for i in clean.clean_data:
            text_arr.append([i, clean.label[0]])

        for i in text_arr:
            query_doc.save_docs_into(i[0], i[1])

        clean2 = pre_process.get_clean_data("https://en.wikipedia.org/wiki/Medicine", "medicine")

        text_arr = []

        for i in clean2.clean_data:
            text_arr.append([i, clean2.label[0]])

        for i in text_arr:
            query_doc.save_docs_into(i[0], i[1])


    except Exception as e:

        print(e)

def finds_users_input_subject():
    users_new_url = input("please enter url:")

    clean_user_text = pre_process.get_clean_data(f"{users_new_url}","")
    print(find_tf_idf.finding_label_of_new_file([clean_user_text.clean_data[4], ""], query_doc.get_docs()))


system_first_uploading()
finds_users_input_subject()
# clean3 = pre_process.get_clean_data("https://en.wikipedia.org/wiki/Tel_Aviv", "other")
# clean4 = pre_process.get_clean_data("https://en.wikipedia.org/wiki/Football")
#     print(find_tf_idf.finding_label_of_new_file([clean2.clean_data[2], ""], query_doc.get_docs()))

# print(query_doc.get_docs())

# print(find_tf_idf.finds_list_of_all_documents_terms_values(query_doc.get_docs()))
