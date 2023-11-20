
def getPromptForComplianceReport(compliance_webpage_extracted_text : str, target_webpage_extracted_text : str) -> str:

    formatted_prompt = f"""
    I have extracted text from two webpages. The first text is from a webpage that outlines compliance policies, and the second text is from a webpage that needs to be checked against these compliance policies. I require a detailed compliance report that identifies any discrepancies or non-compliance in the second webpage's content based on the guidelines provided in the first.

    Text from Compliance Policy Webpage:
    {compliance_webpage_extracted_text}
    
    Text from Webpage to be Checked for Compliance:
    {target_webpage_extracted_text}
    
    Task:
    Please analyze the text from both webpages. Generate a compliance report that highlights the following:
    
    Instances of Non-Compliance: Identify any use of prohibited terms, concepts, or phrases from the compliance policy in the webpage's content. Highlight specific sections or phrases where these discrepancies occur.
    
    Compliance Adherence: Note any parts of the webpage's content that correctly adhere to the compliance guidelines.
    
    Conclusion: Provide a brief summary of the overall compliance status of the webpage. Include recommendations for addressing any identified areas of non-compliance.
    
    The report should be structured as follows:
    
    Compliance Report:
    Non-Compliance Findings: [Details of non-compliance instances]
    Compliance Adherence: [Details of compliance adherence]
    Conclusion and Recommendations: [Summary and suggestions for improvement]
    Please focus solely on the compliance aspects, avoiding any additional commentary or analysis procedures. The report should be clear, concise, and directly related to the compliance guidelines provided.
    """

    return formatted_prompt
