from iteung import reply


""" data = reply.get_val_data()
val_q = []
val_a = []
bot_a = []
for i, v in data.iterrows():
    val_question = v['0']
    val_answer = v['1'].replace('<START>', '').replace('<END>', '').strip()
    val_q.append(val_question)
    val_a.append(val_answer)
    bot_a.append(reply.botReply(val_question)[0])

bot_test_dataframe = pd.DataFrame(
    {
        'question': val_q,
        'answer': val_a,
        'bot': bot_a
    }
)

reply.bot_test_dataframe.to_csv('output_dir/test_result.csv', index=False) """

while True:
    message = input("Kamu: ")
    return_message, status = reply.botReply(message)
    print(f"ITeung: {return_message}")