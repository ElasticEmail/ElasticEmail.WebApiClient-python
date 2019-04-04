'''
The MIT License (MIT)

Copyright (c) 2016-2017 Elastic Email, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import requests
import json
from enum import Enum

# API version 2.42.0
class ApiClient:
	apiUri = 'https://api.elasticemail.com/v2'
	apiKey = '00000000-0000-0000-0000-0000000000000'

	def Request(method, url, data=dict(), attachs=None):
		data['apikey'] = ApiClient.apiKey
		if method == 'POST':
			result = requests.post(ApiClient.apiUri + url, params = data, files = attachs)
		elif method == 'PUT':
			result = requests.put(ApiClient.apiUri + url, params = data)
		elif method == 'GET':
			attach = ''
			params = { k: v for k, v in data.items() if v != None } 
			result = requests.get(ApiClient.apiUri + url, params = params) 
			print(result.url) 	
			
		jsonMy = result.json()
		
		if jsonMy['success'] is False:
			return jsonMy['error']
			
		if 'data' in jsonMy.keys():
			return jsonMy['data']
		else:
			return 'success'

    def AddDictionaryParameter(dictionary, paramName, parameters):
        for key in dictionary:
            parameters[paramName + "_" + key] = dictionary[key]


class ApiTypes:
    """
    
    """
    class AccessLevel(Enum):
        """
        
        """
        EENone = 0

        """
        
        """
        ViewAccount = 1

        """
        
        """
        ViewContacts = 2

        """
        
        """
        ViewForms = 4

        """
        
        """
        ViewTemplates = 8

        """
        
        """
        ViewCampaigns = 16

        """
        
        """
        ViewChannels = 32

        """
        
        """
        ViewJourneys = 64

        """
        
        """
        ViewSurveys = 128

        """
        
        """
        ViewSettings = 256

        """
        
        """
        ViewBilling = 512

        """
        
        """
        ViewSubAccounts = 1024

        """
        
        """
        ViewUsers = 2048

        """
        
        """
        ViewFiles = 4096

        """
        
        """
        ViewReports = 8192

        """
        
        """
        ModifyAccount = 16384

        """
        
        """
        ModifyContacts = 32768

        """
        
        """
        ModifyForms = 65536

        """
        
        """
        ModifyTemplates = 131072

        """
        
        """
        ModifyCampaigns = 262144

        """
        
        """
        ModifyChannels = 524288

        """
        
        """
        ModifyJourneys = 1048576

        """
        
        """
        ModifySurveys = 2097152

        """
        
        """
        ModifyFiles = 4194304

        """
        
        """
        Export = 8388608

        """
        
        """
        SendSmtp = 16777216

        """
        
        """
        SendSMS = 33554432

        """
        
        """
        ModifySettings = 67108864

        """
        
        """
        ModifyBilling = 134217728

        """
        
        """
        ModifyProfile = 268435456

        """
        
        """
        ModifySubAccounts = 536870912

        """
        
        """
        ModifyUsers = 1073741824

        """
        
        """
        Security = 2147483648

        """
        
        """
        ModifyLanguage = 4294967296

        """
        
        """
        ModifySupport = 8589934592

        """
        
        """
        ViewSupport = 8589934592

        """
        
        """
        SendHttp = 17179869184


    """
    
    """
    class AccessToken:
        """
        Access which this Token grants
        """
        AccessLevel = None #ApiTypes.AccessLevel

        """
        Filename
        """
        Name = None #string

        """
        When was this AccessToken used last
        """
        LastUse = None #DateTime?


    """
    Detailed information about your account
    """
    class Account:
        """
        Code used for tax purposes.
        """
        TaxCode = None #string

        """
        Public key for limited access to your account such as contact/add so you can use it safely on public websites.
        """
        PublicAccountID = None #string

        """
        ApiKey that gives you access to our SMTP and HTTP API's.
        """
        ApiKey = None #string

        """
        Second ApiKey that gives you access to our SMTP and HTTP API's.  Used mainly for changing ApiKeys without disrupting services.
        """
        ApiKey2 = None #string

        """
        True, if account is a subaccount. Otherwise, false
        """
        IsSub = None #bool

        """
        The number of subaccounts this account has.
        """
        SubAccountsCount = None #long

        """
        Number of status: 1 - Active
        """
        StatusNumber = None #int

        """
        Account status: Active
        """
        StatusFormatted = None #string

        """
        URL form for payments.
        """
        PaymentFormUrl = None #string

        """
        URL to your logo image.
        """
        LogoUrl = None #string

        """
        HTTP address of your website.
        """
        Website = None #string

        """
        True: Turn on or off ability to send mails under your brand. Otherwise, false
        """
        EnablePrivateBranding = None #bool

        """
        Address to your support.
        """
        SupportLink = None #string

        """
        Subdomain for your rebranded service
        """
        PrivateBrandingUrl = None #string

        """
        First name.
        """
        FirstName = None #string

        """
        Last name.
        """
        LastName = None #string

        """
        Company name.
        """
        Company = None #string

        """
        First line of address.
        """
        Address1 = None #string

        """
        Second line of address.
        """
        Address2 = None #string

        """
        City.
        """
        City = None #string

        """
        State or province.
        """
        State = None #string

        """
        Zip/postal code.
        """
        Zip = None #string

        """
        Numeric ID of country. A file with the list of countries is available <a href="http://api.elasticemail.com/public/countries"><b>here</b></a>
        """
        CountryID = None #int?

        """
        Phone number
        """
        Phone = None #string

        """
        Proper email address.
        """
        Email = None #string

        """
        URL for affiliating.
        """
        AffiliateLink = None #string

        """
        Numeric reputation
        """
        Reputation = None #double

        """
        Amount of emails sent from this account
        """
        TotalEmailsSent = None #long

        """
        Amount of emails sent from this account
        """
        MonthlyEmailsSent = None #long?

        """
        Amount of emails sent from this account
        """
        Credit = None #decimal

        """
        Amount of email credits
        """
        EmailCredits = None #int

        """
        Amount of emails sent from this account
        """
        PricePerEmail = None #decimal

        """
        Why your clients are receiving your emails.
        """
        DeliveryReason = None #string

        """
        URL for making payments.
        """
        AccountPaymentUrl = None #string

        """
        Address of SMTP server.
        """
        Smtp = None #string

        """
        Address of alternative SMTP server.
        """
        SmtpAlternative = None #string

        """
        Status of automatic payments configuration.
        """
        AutoCreditStatus = None #string

        """
        When AutoCreditStatus is Enabled, the credit level that triggers the credit to be recharged.
        """
        AutoCreditLevel = None #decimal

        """
        When AutoCreditStatus is Enabled, the amount of credit to be recharged.
        """
        AutoCreditAmount = None #decimal

        """
        Amount of emails account can send daily
        """
        DailySendLimit = None #int

        """
        Creation date.
        """
        DateCreated = None #DateTime

        """
        True, if you have enabled link tracking. Otherwise, false
        """
        LinkTracking = None #bool

        """
        Type of content encoding
        """
        ContentTransferEncoding = None #string

        """
        Amount of Litmus credits
        """
        LitmusCredits = None #decimal

        """
        Enable contact delivery and optimization tools on your Account.
        """
        EnableContactFeatures = None #bool

        """
        
        """
        NeedsSMSVerification = None #bool

        """
        
        """
        DisableGlobalContacts = None #bool


    """
    Basic overview of your account
    """
    class AccountOverview:
        """
        Amount of emails sent from this account
        """
        TotalEmailsSent = None #long

        """
        Amount of emails sent from this account
        """
        Credit = None #decimal

        """
        Cost of 1000 emails
        """
        CostPerThousand = None #decimal

        """
        Number of messages in progress
        """
        InProgressCount = None #long

        """
        Number of contacts currently with blocked status of Unsubscribed, Complaint, Bounced or InActive
        """
        BlockedContactsCount = None #long

        """
        Numeric reputation
        """
        Reputation = None #double

        """
        Number of contacts
        """
        ContactCount = None #long

        """
        Number of created campaigns
        """
        CampaignCount = None #long

        """
        Number of available templates
        """
        TemplateCount = None #long

        """
        Number of created subaccounts
        """
        SubAccountCount = None #long

        """
        Number of active referrals
        """
        ReferralCount = None #long


    """
    Lists advanced sending options of your account.
    """
    class AdvancedOptions:
        """
        True, if you want to track clicks. Otherwise, false
        """
        EnableClickTracking = None #bool

        """
        True, if you want to track by link tracking. Otherwise, false
        """
        EnableLinkClickTracking = None #bool

        """
        True, if you want to use template scripting in your emails {{}}. Otherwise, false
        """
        EnableTemplateScripting = None #bool

        """
        True, if text BODY of message should be created automatically. Otherwise, false
        """
        AutoTextFormat = None #bool

        """
        True, if you want bounce notifications returned. Otherwise, false
        """
        EmailNotificationForError = None #bool

        """
        True, if you want to send web notifications for sent email. Otherwise, false
        """
        WebNotificationForSent = None #bool

        """
        True, if you want to send web notifications for opened email. Otherwise, false
        """
        WebNotificationForOpened = None #bool

        """
        True, if you want to send web notifications for clicked email. Otherwise, false
        """
        WebNotificationForClicked = None #bool

        """
        True, if you want to send web notifications for unsubscribed email. Otherwise, false
        """
        WebnotificationForUnsubscribed = None #bool

        """
        True, if you want to send web notifications for complaint email. Otherwise, false
        """
        WebNotificationForAbuse = None #bool

        """
        True, if you want to send web notifications for bounced email. Otherwise, false
        """
        WebNotificationForError = None #bool

        """
        True, if you want to receive notifications for each type only once per email. Otherwise, false
        """
        WebNotificationNotifyOncePerEmail = None #bool

        """
        True, if you want to receive low credit email notifications. Otherwise, false
        """
        LowCreditNotification = None #bool

        """
        True, if you want inbound email to only process contacts from your account. Otherwise, false
        """
        InboundContactsOnly = None #bool

        """
        True, if this account is a sub-account. Otherwise, false
        """
        IsSubAccount = None #bool

        """
        True, if this account resells Elastic Email. Otherwise, false.
        """
        IsOwnedByReseller = None #bool

        """
        True, if you want to enable list-unsubscribe header. Otherwise, false
        """
        EnableUnsubscribeHeader = None #bool

        """
        True, if you want to display your labels on your unsubscribe form. Otherwise, false
        """
        ManageSubscriptions = None #bool

        """
        True, if you want to only display labels that the contact is subscribed to on your unsubscribe form. Otherwise, false
        """
        ManageSubscribedOnly = None #bool

        """
        True, if you want to display an option for the contact to opt into transactional email only on your unsubscribe form. Otherwise, false
        """
        TransactionalOnUnsubscribe = None #bool

        """
        
        """
        ConsentTrackingOnUnsubscribe = None #bool

        """
        
        """
        PreviewMessageID = None #string

        """
        True, if you want to apply custom headers to your emails. Otherwise, false
        """
        AllowCustomHeaders = None #bool

        """
        Email address to send a copy of all email to.
        """
        BccEmail = None #string

        """
        Type of content encoding
        """
        ContentTransferEncoding = None #string

        """
        True, if you want to receive bounce email notifications. Otherwise, false
        """
        EmailNotification = None #string

        """
        Email addresses to send a copy of all notifications from our system. Separated by semicolon
        """
        NotificationsEmails = None #string

        """
        Emails, separated by semicolon, to which the notification about contact unsubscribing should be sent to
        """
        UnsubscribeNotificationEmails = None #string

        """
        URL address to receive web notifications to parse and process.
        """
        WebNotificationUrl = None #string

        """
        URL used for tracking action of inbound emails
        """
        HubCallbackUrl = None #string

        """
        Domain you use as your inbound domain
        """
        InboundDomain = None #string

        """
        True, if account has tooltips active. Otherwise, false
        """
        EnableUITooltips = None #bool

        """
        True, if you want to use Contact Delivery Tools.  Otherwise, false
        """
        EnableContactFeatures = None #bool

        """
        URL to your logo image.
        """
        LogoUrl = None #string

        """
        (0 means this functionality is NOT enabled) Score, depending on the number of times you have sent to a recipient, at which the given recipient should be moved to the Stale status
        """
        StaleContactScore = None #int

        """
        (0 means this functionality is NOT enabled) Number of days of inactivity for a contact after which the given recipient should be moved to the Stale status
        """
        StaleContactInactiveDays = None #int

        """
        Why your clients are receiving your emails.
        """
        DeliveryReason = None #string


    """
    Blocked Contact - Contact returning Hard Bounces
    """
    class BlockedContact:
        """
        Proper email address.
        """
        Email = None #string

        """
        Name of status: Active, Engaged, Inactive, Abuse, Bounced, Unsubscribed.
        """
        Status = None #string

        """
        RFC error message
        """
        FriendlyErrorMessage = None #string

        """
        Last change date
        """
        DateUpdated = None #string


    """
    Summary of bounced categories, based on specified date range.
    """
    class BouncedCategorySummary:
        """
        Number of messages marked as SPAM
        """
        Spam = None #long

        """
        Number of blacklisted messages
        """
        BlackListed = None #long

        """
        Number of messages flagged with 'No Mailbox'
        """
        NoMailbox = None #long

        """
        Number of messages flagged with 'Grey Listed'
        """
        GreyListed = None #long

        """
        Number of messages flagged with 'Throttled'
        """
        Throttled = None #long

        """
        Number of messages flagged with 'Timeout'
        """
        Timeout = None #long

        """
        Number of messages flagged with 'Connection Problem'
        """
        ConnectionProblem = None #long

        """
        Number of messages flagged with 'SPF Problem'
        """
        SpfProblem = None #long

        """
        Number of messages flagged with 'Account Problem'
        """
        AccountProblem = None #long

        """
        Number of messages flagged with 'DNS Problem'
        """
        DnsProblem = None #long

        """
        Number of messages flagged with 'WhiteListing Problem'
        """
        WhitelistingProblem = None #long

        """
        Number of messages flagged with 'Code Error'
        """
        CodeError = None #long

        """
        Number of messages flagged with 'Not Delivered'
        """
        NotDelivered = None #long

        """
        Number of manually cancelled messages
        """
        ManualCancel = None #long

        """
        Number of messages flagged with 'Connection terminated'
        """
        ConnectionTerminated = None #long


    """
    Campaign
    """
    class Campaign:
        """
        ID number of selected Channel.
        """
        ChannelID = None #int?

        """
        Campaign's name
        """
        Name = None #string

        """
        Name of campaign's status
        """
        Status = None #ApiTypes.CampaignStatus

        """
        List of Segment and List IDs, preceded with 'l' for Lists and 's' for Segments, comma separated
        """
        Targets = None #string[]

        """
        Number of event, triggering mail sending
        """
        TriggerType = None #ApiTypes.CampaignTriggerType

        """
        Date of triggered send
        """
        TriggerDate = None #DateTime?

        """
        How far into the future should the campaign be sent, in minutes
        """
        TriggerDelay = None #double

        """
        When your next automatic mail will be sent, in minutes
        """
        TriggerFrequency = None #double

        """
        How many times should the campaign be sent
        """
        TriggerCount = None #int

        """
        ID number of transaction
        """
        TriggerChannelID = None #int

        """
        Data for filtering event campaigns such as specific link addresses.
        """
        TriggerData = None #string

        """
        What should be checked for choosing the winner: opens or clicks
        """
        SplitOptimization = None #ApiTypes.SplitOptimization

        """
        Number of minutes between sends during optimization period
        """
        SplitOptimizationMinutes = None #int

        """
        
        """
        TimingOption = None #int

        """
        Should the opens be tracked? If no value has been provided, account's default setting will be used.
        """
        TrackOpens = None #bool?

        """
        Should the clicks be tracked? If no value has been provided, account's default setting will be used.
        """
        TrackClicks = None #bool?

        """
        
        """
        CampaignTemplates = None #List<ApiTypes.CampaignTemplate>


    """
    Channel
    """
    class CampaignChannel:
        """
        ID number of selected Channel.
        """
        ChannelID = None #int

        """
        Filename
        """
        Name = None #string

        """
        True, if you are sending a campaign. Otherwise, false.
        """
        IsCampaign = None #bool

        """
        Name of your custom IP Pool to be used in the sending process
        """
        PoolName = None #string

        """
        Date of creation in YYYY-MM-DDThh:ii:ss format
        """
        DateAdded = None #DateTime

        """
        Name of campaign's status
        """
        Status = None #ApiTypes.CampaignStatus

        """
        Date of last activity on account
        """
        LastActivity = None #DateTime?

        """
        Datetime of last action done on campaign.
        """
        LastProcessed = None #DateTime?

        """
        Id number of parent channel
        """
        ParentChannelID = None #int

        """
        List of Segment and List IDs, preceded with 'l' for Lists and 's' for Segments, comma separated
        """
        Targets = None #string[]

        """
        Number of event, triggering mail sending
        """
        TriggerType = None #ApiTypes.CampaignTriggerType

        """
        Date of triggered send
        """
        TriggerDate = None #DateTime?

        """
        How far into the future should the campaign be sent, in minutes
        """
        TriggerDelay = None #double

        """
        When your next automatic mail will be sent, in minutes
        """
        TriggerFrequency = None #double

        """
        How many times should the campaign be sent
        """
        TriggerCount = None #int

        """
        ID number of transaction
        """
        TriggerChannelID = None #int

        """
        Data for filtering event campaigns such as specific link addresses.
        """
        TriggerData = None #string

        """
        What should be checked for choosing the winner: opens or clicks
        """
        SplitOptimization = None #ApiTypes.SplitOptimization

        """
        Number of minutes between sends during optimization period
        """
        SplitOptimizationMinutes = None #int

        """
        
        """
        TimingOption = None #int

        """
        ID number of template.
        """
        TemplateID = None #int?

        """
        Default subject of email.
        """
        TemplateSubject = None #string

        """
        Default From: email address.
        """
        TemplateFromEmail = None #string

        """
        Default From: name.
        """
        TemplateFromName = None #string

        """
        Default Reply: email address.
        """
        TemplateReplyEmail = None #string

        """
        Default Reply: name.
        """
        TemplateReplyName = None #string

        """
        Total emails clicked
        """
        ClickedCount = None #int

        """
        Total emails opened.
        """
        OpenedCount = None #int

        """
        Overall number of recipients
        """
        RecipientCount = None #int

        """
        Total emails sent.
        """
        SentCount = None #int

        """
        Total emails failed.
        """
        FailedCount = None #int

        """
        Total emails unsubscribed
        """
        UnsubscribedCount = None #int

        """
        Abuses - mails sent to user without their consent
        """
        FailedAbuse = None #int

        """
        List of CampaignTemplate for sending A-X split testing.
        """
        TemplateChannels = None #List<ApiTypes.CampaignChannel>

        """
        Should the opens be tracked? If no value has been provided, account's default setting will be used.
        """
        TrackOpens = None #bool?

        """
        Should the clicks be tracked? If no value has been provided, account's default setting will be used.
        """
        TrackClicks = None #bool?


    """
    
    """
    class CampaignStatus(Enum):
        """
        Campaign is logically deleted and not returned by API or interface calls.
        """
        Deleted = -1

        """
        Campaign is curently active and available.
        """
        Active = 0

        """
        Campaign is currently being processed for delivery.
        """
        Processing = 1

        """
        Campaign is currently sending.
        """
        Sending = 2

        """
        Campaign has completed sending.
        """
        Completed = 3

        """
        Campaign is currently paused and not sending.
        """
        Paused = 4

        """
        Campaign has been cancelled during delivery.
        """
        Cancelled = 5

        """
        Campaign is save as draft and not processing.
        """
        Draft = 6


    """
    
    """
    class CampaignTemplate:
        """
        ID number of selected Channel.
        """
        ChannelID = None #int?

        """
        Name of campaign's status
        """
        Status = None #ApiTypes.CampaignStatus

        """
        Name of your custom IP Pool to be used in the sending process
        """
        PoolName = None #string

        """
        ID number of template.
        """
        TemplateID = None #int?

        """
        Default subject of email.
        """
        TemplateSubject = None #string

        """
        Default From: email address.
        """
        TemplateFromEmail = None #string

        """
        Default From: name.
        """
        TemplateFromName = None #string

        """
        Default Reply: email address.
        """
        TemplateReplyEmail = None #string

        """
        Default Reply: name.
        """
        TemplateReplyName = None #string


    """
    
    """
    class CampaignTriggerType(Enum):
        """
        
        """
        SendNow = 1

        """
        
        """
        FutureScheduled = 2

        """
        
        """
        OnAdd = 3

        """
        
        """
        OnOpen = 4

        """
        
        """
        OnClick = 5


    """
    
    """
    class CertificateValidationStatus(Enum):
        """
        
        """
        ErrorOccured = -2

        """
        
        """
        CertNotSet = 0

        """
        
        """
        Valid = 1

        """
        
        """
        NotValid = 2


    """
    SMTP and HTTP API channel for grouping email delivery
    """
    class Channel:
        """
        Descriptive name of the channel.
        """
        Name = None #string

        """
        The date the channel was added to your account.
        """
        DateAdded = None #DateTime

        """
        The date the channel was last sent through.
        """
        LastActivity = None #DateTime?

        """
        The number of email jobs this channel has been used with.
        """
        JobCount = None #int

        """
        The number of emails that have been clicked within this channel.
        """
        ClickedCount = None #int

        """
        The number of emails that have been opened within this channel.
        """
        OpenedCount = None #int

        """
        The number of emails attempted to be sent within this channel.
        """
        RecipientCount = None #int

        """
        The number of emails that have been sent within this channel.
        """
        SentCount = None #int

        """
        The number of emails that have been bounced within this channel.
        """
        FailedCount = None #int

        """
        The number of emails that have been unsubscribed within this channel.
        """
        UnsubscribedCount = None #int

        """
        The number of emails that have been marked as abuse or complaint within this channel.
        """
        FailedAbuse = None #int

        """
        The total cost for emails/attachments within this channel.
        """
        Cost = None #decimal


    """
    FileResponse compression format
    """
    class CompressionFormat(Enum):
        """
        No compression
        """
        EENone = 0

        """
        Zip compression
        """
        Zip = 1


    """
    
    """
    class ConsentTracking(Enum):
        """
        
        """
        Unknown = 0

        """
        
        """
        Allow = 1

        """
        
        """
        Deny = 2


    """
    Contact
    """
    class Contact:
        """
        
        """
        ContactScore = None #int

        """
        Date of creation in YYYY-MM-DDThh:ii:ss format
        """
        DateAdded = None #DateTime

        """
        Proper email address.
        """
        Email = None #string

        """
        First name.
        """
        FirstName = None #string

        """
        Last name.
        """
        LastName = None #string

        """
        Name of status: Active, Engaged, Inactive, Abuse, Bounced, Unsubscribed.
        """
        Status = None #ApiTypes.ContactStatus

        """
        RFC Error code
        """
        BouncedErrorCode = None #int?

        """
        RFC error message
        """
        BouncedErrorMessage = None #string

        """
        Total emails sent.
        """
        TotalSent = None #int

        """
        Total emails failed.
        """
        TotalFailed = None #int

        """
        Total emails opened.
        """
        TotalOpened = None #int

        """
        Total emails clicked
        """
        TotalClicked = None #int

        """
        Date of first failed message
        """
        FirstFailedDate = None #DateTime?

        """
        Number of fails in sending to this Contact
        """
        LastFailedCount = None #int

        """
        Last change date
        """
        DateUpdated = None #DateTime

        """
        Source of URL of payment
        """
        Source = None #ApiTypes.ContactSource

        """
        RFC Error code
        """
        ErrorCode = None #int?

        """
        RFC error message
        """
        FriendlyErrorMessage = None #string

        """
        IP address
        """
        CreatedFromIP = None #string

        """
        IP address of consent to send this contact(s) your email. If not provided your current public IP address is used for consent.
        """
        ConsentIP = None #string

        """
        Date of consent to send this contact(s) your email. If not provided current date is used for consent.
        """
        ConsentDate = None #DateTime?

        """
        
        """
        ConsentTracking = None #ApiTypes.ConsentTracking

        """
        Unsubscribed date in YYYY-MM-DD format
        """
        UnsubscribedDate = None #DateTime?

        """
        Free form field of notes
        """
        Notes = None #string

        """
        Website of contact
        """
        WebsiteUrl = None #string

        """
        Date this contact last opened an email
        """
        LastOpened = None #DateTime?

        """
        
        """
        LastClicked = None #DateTime?

        """
        Custom contact field like firstname, lastname, city etc. JSON serialized text like { "city":"london" } 
        """
        CustomFields = None #Dictionary<string, string>


    """
    Collection of lists and segments
    """
    class ContactCollection:
        """
        Lists which contain the requested contact
        """
        Lists = None #List<ApiTypes.ContactContainer>

        """
        Segments which contain the requested contact
        """
        Segments = None #List<ApiTypes.ContactContainer>


    """
    List's or segment's short info
    """
    class ContactContainer:
        """
        ID of the list/segment
        """
        ID = None #int

        """
        Name of the list/segment
        """
        Name = None #string


    """
    
    """
    class ContactHistEventType(Enum):
        """
        Contact opened an e-mail
        """
        Opened = 2

        """
        Contact clicked an e-mail
        """
        Clicked = 3

        """
        E-mail sent to the contact bounced
        """
        Bounced = 10

        """
        Contact unsubscribed
        """
        Unsubscribed = 11

        """
        Contact complained to an e-mail
        """
        Complained = 12

        """
        Contact clicked an activation link
        """
        Activated = 20

        """
        Contact has opted to receive Transactional-only e-mails
        """
        TransactionalUnsubscribed = 21

        """
        Contact's status was changed manually
        """
        ManualStatusChange = 22

        """
        An Activation e-mail was sent
        """
        ActivationSent = 24

        """
        Contact was deleted
        """
        Deleted = 28


    """
    History of chosen Contact
    """
    class ContactHistory:
        """
        ID of history of selected Contact.
        """
        ContactHistoryID = None #long

        """
        Type of event occured on this Contact.
        """
        EventType = None #string

        """
        Numeric code of event occured on this Contact.
        """
        EventTypeValue = None #ApiTypes.ContactHistEventType

        """
        Formatted date of event.
        """
        EventDate = None #string

        """
        Name of selected channel.
        """
        ChannelName = None #string

        """
        Name of template.
        """
        TemplateName = None #string

        """
        IP Address of the event.
        """
        IPAddress = None #string

        """
        Country of the event.
        """
        Country = None #string

        """
        Information about the event
        """
        Data = None #string


    """
    
    """
    class ContactSource(Enum):
        """
        Source of the contact is from sending an email via our SMTP or HTTP API's
        """
        DeliveryApi = 0

        """
        Contact was manually entered from the interface.
        """
        ManualInput = 1

        """
        Contact was uploaded via a file such as CSV.
        """
        FileUpload = 2

        """
        Contact was added from a public web form.
        """
        WebForm = 3

        """
        Contact was added from the contact api.
        """
        ContactApi = 4


    """
    
    """
    class ContactStatus(Enum):
        """
        Only transactional email can be sent to contacts with this status.
        """
        Transactional = -2

        """
        Contact has had an open or click in the last 6 months.
        """
        Engaged = -1

        """
        Contact is eligible to be sent to.
        """
        Active = 0

        """
        Contact has had a hard bounce and is no longer eligible to be sent to.
        """
        Bounced = 1

        """
        Contact has unsubscribed and is no longer eligible to be sent to.
        """
        Unsubscribed = 2

        """
        Contact has complained and is no longer eligible to be sent to.
        """
        Abuse = 3

        """
        Contact has not been activated or has been de-activated and is not eligible to be sent to.
        """
        Inactive = 4

        """
        Contact has not been opening emails for a long period of time and is not eligible to be sent to.
        """
        Stale = 5

        """
        Contact has not confirmed their double opt-in activation and is not eligible to be sent to.
        """
        NotConfirmed = 6


    """
    Number of Contacts, grouped by Status;
    """
    class ContactStatusCounts:
        """
        Number of engaged contacts
        """
        Engaged = None #long

        """
        Number of active contacts
        """
        Active = None #long

        """
        Number of complaint messages
        """
        Complaint = None #long

        """
        Number of unsubscribed messages
        """
        Unsubscribed = None #long

        """
        Number of bounced messages
        """
        Bounced = None #long

        """
        Number of inactive contacts
        """
        Inactive = None #long

        """
        Number of transactional contacts
        """
        Transactional = None #long

        """
        
        """
        Stale = None #long

        """
        
        """
        NotConfirmed = None #long


    """
    Number of Unsubscribed or Complaint Contacts, grouped by Unsubscribe Reason;
    """
    class ContactUnsubscribeReasonCounts:
        """
        
        """
        Unknown = None #long

        """
        
        """
        NoLongerWant = None #long

        """
        
        """
        IrrelevantContent = None #long

        """
        
        """
        TooFrequent = None #long

        """
        
        """
        NeverConsented = None #long

        """
        
        """
        DeceptiveContent = None #long

        """
        
        """
        AbuseReported = None #long

        """
        
        """
        ThirdParty = None #long

        """
        
        """
        ListUnsubscribe = None #long


    """
    Type of credits
    """
    class CreditType(Enum):
        """
        Used to send emails.  One credit = one email.
        """
        Email = 9

        """
        Used to run a litmus test on a template.  1 credit = 1 test.
        """
        Litmus = 11


    """
    Daily summary of log status, based on specified date range.
    """
    class DailyLogStatusSummary:
        """
        Date in YYYY-MM-DDThh:ii:ss format
        """
        Date = None #string

        """
        Proper email address.
        """
        Email = None #int

        """
        Number of SMS
        """
        Sms = None #int

        """
        Number of delivered messages
        """
        Delivered = None #int

        """
        Number of opened messages
        """
        Opened = None #int

        """
        Number of clicked messages
        """
        Clicked = None #int

        """
        Number of unsubscribed messages
        """
        Unsubscribed = None #int

        """
        Number of complaint messages
        """
        Complaint = None #int

        """
        Number of bounced messages
        """
        Bounced = None #int

        """
        Number of inbound messages
        """
        Inbound = None #int

        """
        Number of manually cancelled messages
        """
        ManualCancel = None #int

        """
        Number of messages flagged with 'Not Delivered'
        """
        NotDelivered = None #int


    """
    Domain data, with information about domain records.
    """
    class DomainDetail:
        """
        Name of selected domain.
        """
        Domain = None #string

        """
        True, if domain is used as default. Otherwise, false,
        """
        DefaultDomain = None #bool

        """
        True, if SPF record is verified
        """
        Spf = None #bool

        """
        True, if DKIM record is verified
        """
        Dkim = None #bool

        """
        True, if MX record is verified
        """
        MX = None #bool

        """
        
        """
        DMARC = None #bool

        """
        True, if tracking CNAME record is verified
        """
        IsRewriteDomainValid = None #bool

        """
        True, if verification is available
        """
        Verify = None #bool

        """
        
        """
        Type = None #ApiTypes.TrackingType

        """
        0 - NotValidated, 1 - Validated successfully, 2 - Invalid, 3 - Broken (tracking was frequnetly verfied in given period and still is invalid). For statuses: 0, 1, 3 tracking will be verified in normal periods. For status 2 tracking will be verified in high frequent periods.
        """
        TrackingStatus = None #ApiTypes.TrackingValidationStatus

        """
        
        """
        CertificateStatus = None #ApiTypes.CertificateValidationStatus

        """
        
        """
        CertificateValidationError = None #string

        """
        
        """
        TrackingTypeUserRequest = None #ApiTypes.TrackingType?


    """
    Detailed information about email credits
    """
    class EmailCredits:
        """
        Date in YYYY-MM-DDThh:ii:ss format
        """
        Date = None #DateTime

        """
        Amount of money in transaction
        """
        Amount = None #decimal

        """
        Source of URL of payment
        """
        Source = None #string

        """
        Free form field of notes
        """
        Notes = None #string


    """
    
    """
    class EmailJobFailedStatus:
        """
        
        """
        Address = None #string

        """
        
        """
        Error = None #string

        """
        RFC Error code
        """
        ErrorCode = None #int

        """
        
        """
        Category = None #string


    """
    
    """
    class EmailJobStatus:
        """
        ID number of your attachment
        """
        ID = None #string

        """
        Name of status: submitted, complete, in_progress
        """
        Status = None #string

        """
        
        """
        RecipientsCount = None #int

        """
        
        """
        Failed = None #List<ApiTypes.EmailJobFailedStatus>

        """
        Total emails failed.
        """
        FailedCount = None #int

        """
        
        """
        Sent = None #List<string>

        """
        Total emails sent.
        """
        SentCount = None #int

        """
        Number of delivered messages
        """
        Delivered = None #List<string>

        """
        
        """
        DeliveredCount = None #int

        """
        
        """
        Pending = None #List<string>

        """
        
        """
        PendingCount = None #int

        """
        Number of opened messages
        """
        Opened = None #List<string>

        """
        Total emails opened.
        """
        OpenedCount = None #int

        """
        Number of clicked messages
        """
        Clicked = None #List<string>

        """
        Total emails clicked
        """
        ClickedCount = None #int

        """
        Number of unsubscribed messages
        """
        Unsubscribed = None #List<string>

        """
        Total emails unsubscribed
        """
        UnsubscribedCount = None #int

        """
        
        """
        AbuseReports = None #List<string>

        """
        
        """
        AbuseReportsCount = None #int

        """
        List of all MessageIDs for this job.
        """
        MessageIDs = None #List<string>


    """
    
    """
    class EmailSend:
        """
        ID number of transaction
        """
        TransactionID = None #string

        """
        Unique identifier for this email.
        """
        MessageID = None #string


    """
    Status information of the specified email
    """
    class EmailStatus:
        """
        Email address this email was sent from.
        """
        From = None #string

        """
        Email address this email was sent to.
        """
        To = None #string

        """
        Date the email was submitted.
        """
        Date = None #DateTime

        """
        Value of email's status
        """
        Status = None #ApiTypes.LogJobStatus

        """
        Name of email's status
        """
        StatusName = None #string

        """
        Date of last status change.
        """
        StatusChangeDate = None #DateTime

        """
        Date when the email was sent
        """
        DateSent = None #DateTime

        """
        Date when the email changed the status to 'opened'
        """
        DateOpened = None #DateTime?

        """
        Date when the email changed the status to 'clicked'
        """
        DateClicked = None #DateTime?

        """
        Detailed error or bounced message.
        """
        ErrorMessage = None #string

        """
        ID number of transaction
        """
        TransactionID = None #Guid


    """
    Email details formatted in json
    """
    class EmailView:
        """
        Body (text) of your message.
        """
        Body = None #string

        """
        Default subject of email.
        """
        Subject = None #string

        """
        Starting date for search in YYYY-MM-DDThh:mm:ss format.
        """
        From = None #string


    """
    Encoding type for the email headers
    """
    class EncodingType(Enum):
        """
        Encoding of the email is provided by the sender and not altered.
        """
        UserProvided = -1

        """
        No endcoding is set for the email.
        """
        EENone = 0

        """
        Encoding of the email is in Raw7bit format.
        """
        Raw7bit = 1

        """
        Encoding of the email is in Raw8bit format.
        """
        Raw8bit = 2

        """
        Encoding of the email is in QuotedPrintable format.
        """
        QuotedPrintable = 3

        """
        Encoding of the email is in Base64 format.
        """
        Base64 = 4

        """
        Encoding of the email is in Uue format.
        """
        Uue = 5


    """
    Record of exported data from the system.
    """
    class Export:
        """
        
        """
        PublicExportID = None #Guid

        """
        Date the export was created
        """
        DateAdded = None #DateTime

        """
        Type of export
        """
        Type = None #string

        """
        Current status of export
        """
        Status = None #string

        """
        Long description of the export
        """
        Info = None #string

        """
        Name of the file
        """
        Filename = None #string

        """
        Link to download the export
        """
        Link = None #string

        """
        Log start date (for Type = Log only)
        """
        LogFrom = None #DateTime?

        """
        Log end date (for Type = Log only)
        """
        LogTo = None #DateTime?


    """
    Type of export
    """
    class ExportFileFormats(Enum):
        """
        Export in comma separated values format.
        """
        Csv = 1

        """
        Export in xml format
        """
        Xml = 2

        """
        Export in json format
        """
        Json = 3


    """
    
    """
    class ExportLink:
        """
        Direct URL to the exported file
        """
        Link = None #string


    """
    Current status of export
    """
    class ExportStatus(Enum):
        """
        Export had an error and can not be downloaded.
        """
        Error = -1

        """
        Export is currently loading and can not be downloaded.
        """
        Loading = 0

        """
        Export is currently available for downloading.
        """
        Ready = 1

        """
        Export is no longer available for downloading.
        """
        Expired = 2


    """
    Number of Exports, grouped by export type
    """
    class ExportTypeCounts:
        """
        
        """
        Log = None #long

        """
        
        """
        Contact = None #long

        """
        Json representation of a campaign
        """
        Campaign = None #long

        """
        True, if you have enabled link tracking. Otherwise, false
        """
        LinkTracking = None #long

        """
        Json representation of a survey
        """
        Survey = None #long


    """
    
    """
    class File:
        """
        Name of your file.
        """
        FileName = None #string

        """
        Size of your attachment (in bytes).
        """
        Size = None #int?

        """
        Date of creation in YYYY-MM-DDThh:ii:ss format
        """
        DateAdded = None #DateTime

        """
        When will the file be deleted from the system
        """
        ExpirationDate = None #DateTime?

        """
        Content type of the file
        """
        ContentType = None #string


    """
    
    """
    class IntervalType(Enum):
        """
        Daily overview
        """
        Summary = 0

        """
        Hourly, detailed information
        """
        Hourly = 1


    """
    Object containig tracking data.
    """
    class LinkTrackingDetails:
        """
        Number of items.
        """
        Count = None #int

        """
        True, if there are more detailed data available. Otherwise, false
        """
        MoreAvailable = None #bool

        """
        
        """
        TrackedLink = None #List<ApiTypes.TrackedLink>


    """
    List of Lists, with detailed data about its contents.
    """
    class List:
        """
        ID number of selected list.
        """
        ListID = None #int

        """
        Name of your list.
        """
        ListName = None #string

        """
        Number of items.
        """
        Count = None #int

        """
        ID code of list
        """
        PublicListID = None #Guid?

        """
        Date of creation in YYYY-MM-DDThh:ii:ss format
        """
        DateAdded = None #DateTime

        """
        True: Allow unsubscribing from this list. Otherwise, false
        """
        AllowUnsubscribe = None #bool

        """
        Query used for filtering.
        """
        Rule = None #string


    """
    Detailed information about litmus credits
    """
    class LitmusCredits:
        """
        Date in YYYY-MM-DDThh:ii:ss format
        """
        Date = None #DateTime

        """
        Amount of money in transaction
        """
        Amount = None #decimal


    """
    Logs for selected date range
    """
    class Log:
        """
        Starting date for search in YYYY-MM-DDThh:mm:ss format.
        """
        From = None #DateTime?

        """
        Ending date for search in YYYY-MM-DDThh:mm:ss format.
        """
        To = None #DateTime?

        """
        Number of recipients
        """
        Recipients = None #List<ApiTypes.Recipient>


    """
    
    """
    class LogJobStatus(Enum):
        """
        All emails
        """
        All = 0

        """
        Email has been submitted successfully and is queued for sending.
        """
        ReadyToSend = 1

        """
        Email has soft bounced and is scheduled to retry.
        """
        WaitingToRetry = 2

        """
        Email is currently sending.
        """
        Sending = 3

        """
        Email has errored or bounced for some reason.
        """
        Error = 4

        """
        Email has been successfully delivered.
        """
        Sent = 5

        """
        Email has been opened by the recipient.
        """
        Opened = 6

        """
        Email has had at least one link clicked by the recipient.
        """
        Clicked = 7

        """
        Email has been unsubscribed by the recipient.
        """
        Unsubscribed = 8

        """
        Email has been complained about or marked as spam by the recipient.
        """
        AbuseReport = 9


    """
    Summary of log status, based on specified date range.
    """
    class LogStatusSummary:
        """
        Starting date for search in YYYY-MM-DDThh:mm:ss format.
        """
        From = None #string

        """
        Ending date for search in YYYY-MM-DDThh:mm:ss format.
        """
        To = None #string

        """
        Overall duration
        """
        Duration = None #double

        """
        Number of recipients
        """
        Recipients = None #long

        """
        Number of emails
        """
        EmailTotal = None #long

        """
        Number of SMS
        """
        SmsTotal = None #long

        """
        Number of delivered messages
        """
        Delivered = None #long

        """
        Number of bounced messages
        """
        Bounced = None #long

        """
        Number of messages in progress
        """
        InProgress = None #long

        """
        Number of opened messages
        """
        Opened = None #long

        """
        Number of clicked messages
        """
        Clicked = None #long

        """
        Number of unsubscribed messages
        """
        Unsubscribed = None #long

        """
        Number of complaint messages
        """
        Complaints = None #long

        """
        Number of inbound messages
        """
        Inbound = None #long

        """
        Number of manually cancelled messages
        """
        ManualCancel = None #long

        """
        Number of messages flagged with 'Not Delivered'
        """
        NotDelivered = None #long

        """
        ID number of template used
        """
        TemplateChannel = None #bool


    """
    Overall log summary information.
    """
    class LogSummary:
        """
        Summary of log status, based on specified date range.
        """
        LogStatusSummary = None #ApiTypes.LogStatusSummary

        """
        Summary of bounced categories, based on specified date range.
        """
        BouncedCategorySummary = None #ApiTypes.BouncedCategorySummary

        """
        Daily summary of log status, based on specified date range.
        """
        DailyLogStatusSummary = None #List<ApiTypes.DailyLogStatusSummary>


    """
    
    """
    class MessageCategory(Enum):
        """
        
        """
        Unknown = 0

        """
        
        """
        Ignore = 1

        """
        Number of messages marked as SPAM
        """
        Spam = 2

        """
        Number of blacklisted messages
        """
        BlackListed = 3

        """
        Number of messages flagged with 'No Mailbox'
        """
        NoMailbox = 4

        """
        Number of messages flagged with 'Grey Listed'
        """
        GreyListed = 5

        """
        Number of messages flagged with 'Throttled'
        """
        Throttled = 6

        """
        Number of messages flagged with 'Timeout'
        """
        Timeout = 7

        """
        Number of messages flagged with 'Connection Problem'
        """
        ConnectionProblem = 8

        """
        Number of messages flagged with 'SPF Problem'
        """
        SPFProblem = 9

        """
        Number of messages flagged with 'Account Problem'
        """
        AccountProblem = 10

        """
        Number of messages flagged with 'DNS Problem'
        """
        DNSProblem = 11

        """
        
        """
        NotDeliveredCancelled = 12

        """
        Number of messages flagged with 'Code Error'
        """
        CodeError = 13

        """
        Number of manually cancelled messages
        """
        ManualCancel = 14

        """
        Number of messages flagged with 'Connection terminated'
        """
        ConnectionTerminated = 15

        """
        Number of messages flagged with 'Not Delivered'
        """
        NotDelivered = 16


    """
    Queue of notifications
    """
    class NotificationQueue:
        """
        Creation date.
        """
        DateCreated = None #string

        """
        Date of last status change.
        """
        StatusChangeDate = None #string

        """
        Actual status.
        """
        NewStatus = None #string

        """
        
        """
        Reference = None #string

        """
        Error message.
        """
        ErrorMessage = None #string

        """
        Number of previous delivery attempts
        """
        RetryCount = None #string


    """
    
    """
    class NotificationType(Enum):
        """
        Both, email and web, notifications
        """
        All = 0

        """
        Only email notifications
        """
        Email = 1

        """
        Only web notifications
        """
        Web = 2


    """
    Detailed information about existing money transfers.
    """
    class Payment:
        """
        Date in YYYY-MM-DDThh:ii:ss format
        """
        Date = None #DateTime

        """
        Amount of money in transaction
        """
        Amount = None #decimal

        """
        Source of URL of payment
        """
        Source = None #string


    """
    Basic information about your profile
    """
    class Profile:
        """
        First name.
        """
        FirstName = None #string

        """
        Last name.
        """
        LastName = None #string

        """
        Company name.
        """
        Company = None #string

        """
        First line of address.
        """
        Address1 = None #string

        """
        Second line of address.
        """
        Address2 = None #string

        """
        City.
        """
        City = None #string

        """
        State or province.
        """
        State = None #string

        """
        Zip/postal code.
        """
        Zip = None #string

        """
        Numeric ID of country. A file with the list of countries is available <a href="http://api.elasticemail.com/public/countries"><b>here</b></a>
        """
        CountryID = None #int?

        """
        Phone number
        """
        Phone = None #string

        """
        Proper email address.
        """
        Email = None #string

        """
        Code used for tax purposes.
        """
        TaxCode = None #string


    """
    
    """
    class QuestionType(Enum):
        """
        
        """
        RadioButtons = 1

        """
        
        """
        DropdownMenu = 2

        """
        
        """
        Checkboxes = 3

        """
        
        """
        LongAnswer = 4

        """
        
        """
        Textbox = 5

        """
        Date in YYYY-MM-DDThh:ii:ss format
        """
        Date = 6


    """
    Detailed information about message recipient
    """
    class Recipient:
        """
        True, if message is SMS. Otherwise, false
        """
        IsSms = None #bool

        """
        ID number of selected message.
        """
        MsgID = None #string

        """
        Ending date for search in YYYY-MM-DDThh:mm:ss format.
        """
        To = None #string

        """
        Name of recipient's status: Submitted, ReadyToSend, WaitingToRetry, Sending, Bounced, Sent, Opened, Clicked, Unsubscribed, AbuseReport
        """
        Status = None #string

        """
        Name of selected Channel.
        """
        Channel = None #string

        """
        Creation date
        """
        Date = None #string

        """
        Date when the email was sent
        """
        DateSent = None #string

        """
        Date when the email changed the status to 'opened'
        """
        DateOpened = None #string

        """
        Date when the email changed the status to 'clicked'
        """
        DateClicked = None #string

        """
        Content of message, HTML encoded
        """
        Message = None #string

        """
        True, if message category should be shown. Otherwise, false
        """
        ShowCategory = None #bool

        """
        Name of message category
        """
        MessageCategory = None #string

        """
        ID of message category
        """
        MessageCategoryID = None #ApiTypes.MessageCategory

        """
        Date of last status change.
        """
        StatusChangeDate = None #string

        """
        Date of next try
        """
        NextTryOn = None #string

        """
        Default subject of email.
        """
        Subject = None #string

        """
        Default From: email address.
        """
        FromEmail = None #string

        """
        ID of certain mail job
        """
        JobID = None #string

        """
        True, if message is a SMS and status is not yet confirmed. Otherwise, false
        """
        SmsUpdateRequired = None #bool

        """
        Content of message
        """
        TextMessage = None #string

        """
        Comma separated ID numbers of messages.
        """
        MessageSid = None #string

        """
        Recipient's last bounce error because of which this e-mail was suppressed
        """
        ContactLastError = None #string


    """
    Referral details for this account.
    """
    class Referral:
        """
        Current amount of dolars you have from referring.
        """
        CurrentReferralCredit = None #decimal

        """
        Number of active referrals.
        """
        CurrentReferralCount = None #long


    """
    Detailed sending reputation of your account.
    """
    class ReputationDetail:
        """
        Overall reputation impact, based on the most important factors.
        """
        Impact = None #ApiTypes.ReputationImpact

        """
        Percent of Complaining users - those, who do not want to receive email from you.
        """
        AbusePercent = None #double

        """
        Percent of Unknown users - users that couldn't be found
        """
        UnknownUsersPercent = None #double

        """
        
        """
        OpenedPercent = None #double

        """
        
        """
        ClickedPercent = None #double

        """
        Penalty from messages marked as spam.
        """
        AverageSpamScore = None #double

        """
        Percent of Bounced users
        """
        FailedSpamPercent = None #double

        """
        Points from quantity of your emails.
        """
        RepEmailsSent = None #double

        """
        Average reputation.
        """
        AverageReputation = None #double

        """
        Actual price level.
        """
        PriceLevelReputation = None #double

        """
        Reputation needed to change pricing.
        """
        NextPriceLevelReputation = None #double

        """
        Amount of emails sent from this account
        """
        PriceLevel = None #string

        """
        True, if tracking domain is correctly configured. Otherwise, false.
        """
        TrackingDomainValid = None #bool

        """
        True, if sending domain is correctly configured. Otherwise, false.
        """
        SenderDomainValid = None #bool


    """
    Reputation history of your account.
    """
    class ReputationHistory:
        """
        Creation date.
        """
        DateCreated = None #string

        """
        Percent of Complaining users - those, who do not want to receive email from you.
        """
        AbusePercent = None #double

        """
        Percent of Unknown users - users that couldn't be found
        """
        UnknownUsersPercent = None #double

        """
        
        """
        OpenedPercent = None #double

        """
        
        """
        ClickedPercent = None #double

        """
        Penalty from messages marked as spam.
        """
        AverageSpamScore = None #double

        """
        Points from proper setup of your account
        """
        SetupScore = None #double

        """
        Points from quantity of your emails.
        """
        RepEmailsSent = None #double

        """
        Numeric reputation
        """
        Reputation = None #double


    """
    Overall reputation impact, based on the most important factors.
    """
    class ReputationImpact:
        """
        Abuses - mails sent to user without their consent
        """
        Abuse = None #double

        """
        Users, that could not be reached.
        """
        UnknownUsers = None #double

        """
        Number of opened messages
        """
        Opened = None #double

        """
        Number of clicked messages
        """
        Clicked = None #double

        """
        Penalty from messages marked as spam.
        """
        AverageSpamScore = None #double

        """
        Content analysis.
        """
        ServerFilter = None #double

        """
        Tracking domain.
        """
        TrackingDomain = None #double

        """
        Sending domain.
        """
        SenderDomain = None #double


    """
    Information about Contact Segment, selected by RULE.
    """
    class Segment:
        """
        ID number of your segment.
        """
        SegmentID = None #int

        """
        Filename
        """
        Name = None #string

        """
        Query used for filtering.
        """
        Rule = None #string

        """
        Number of items from last check.
        """
        LastCount = None #long

        """
        History of segment information.
        """
        History = None #List<ApiTypes.SegmentHistory>


    """
    Segment History
    """
    class SegmentHistory:
        """
        ID number of history.
        """
        SegmentHistoryID = None #int

        """
        ID number of your segment.
        """
        SegmentID = None #int

        """
        Date in YYYY-MM-DD format
        """
        Day = None #int

        """
        Number of items.
        """
        Count = None #long

        """
        
        """
        EngagedCount = None #long

        """
        
        """
        ActiveCount = None #long

        """
        
        """
        BouncedCount = None #long

        """
        Total emails unsubscribed
        """
        UnsubscribedCount = None #long

        """
        
        """
        AbuseCount = None #long

        """
        
        """
        InactiveCount = None #long


    """
    
    """
    class SendingPermission(Enum):
        """
        Sending not allowed.
        """
        EENone = 0

        """
        Allow sending via SMTP only.
        """
        Smtp = 1

        """
        Allow sending via HTTP API only.
        """
        HttpApi = 2

        """
        Allow sending via SMTP and HTTP API.
        """
        SmtpAndHttpApi = 3

        """
        Allow sending via the website interface only.
        """
        Interface = 4

        """
        Allow sending via SMTP and the website interface.
        """
        SmtpAndInterface = 5

        """
        Allow sendnig via HTTP API and the website interface.
        """
        HttpApiAndInterface = 6

        """
        Use access level sending permission.
        """
        UseAccessLevel = 16

        """
        Sending allowed via SMTP, HTTP API and the website interface.
        """
        All = 255


    """
    Spam check of specified message.
    """
    class SpamCheck:
        """
        Total spam score from
        """
        TotalScore = None #string

        """
        Date in YYYY-MM-DDThh:ii:ss format
        """
        Date = None #string

        """
        Default subject of email.
        """
        Subject = None #string

        """
        Default From: email address.
        """
        FromEmail = None #string

        """
        ID number of selected message.
        """
        MsgID = None #string

        """
        Name of selected channel.
        """
        ChannelName = None #string

        """
        
        """
        Rules = None #List<ApiTypes.SpamRule>


    """
    Single spam score
    """
    class SpamRule:
        """
        Spam score
        """
        Score = None #string

        """
        Name of rule
        """
        Key = None #string

        """
        Description of rule.
        """
        Description = None #string


    """
    
    """
    class SplitOptimization(Enum):
        """
        Number of opened messages
        """
        Opened = 0

        """
        Number of clicked messages
        """
        Clicked = 1


    """
    Subaccount. Contains detailed data of your Subaccount.
    """
    class SubAccount:
        """
        Public key for limited access to your account such as contact/add so you can use it safely on public websites.
        """
        PublicAccountID = None #string

        """
        ApiKey that gives you access to our SMTP and HTTP API's.
        """
        ApiKey = None #string

        """
        Proper email address.
        """
        Email = None #string

        """
        ID number of mailer
        """
        MailerID = None #string

        """
        Name of your custom IP Pool to be used in the sending process
        """
        PoolName = None #string

        """
        Date of last activity on account
        """
        LastActivity = None #string

        """
        Amount of email credits
        """
        EmailCredits = None #string

        """
        True, if account needs credits to send emails. Otherwise, false
        """
        RequiresEmailCredits = None #bool

        """
        Amount of credits added to account automatically
        """
        MonthlyRefillCredits = None #double

        """
        True, if account needs credits to buy templates. Otherwise, false
        """
        RequiresTemplateCredits = None #bool

        """
        Amount of Litmus credits
        """
        LitmusCredits = None #decimal

        """
        True, if account is able to send template tests to Litmus. Otherwise, false
        """
        EnableLitmusTest = None #bool

        """
        True, if account needs credits to send emails. Otherwise, false
        """
        RequiresLitmusCredits = None #bool

        """
        True, if account can buy templates on its own. Otherwise, false
        """
        EnablePremiumTemplates = None #bool

        """
        True, if account can request for private IP on its own. Otherwise, false
        """
        EnablePrivateIPRequest = None #bool

        """
        Amount of emails sent from this account
        """
        TotalEmailsSent = None #long

        """
        Percent of Unknown users - users that couldn't be found
        """
        UnknownUsersPercent = None #double

        """
        Percent of Complaining users - those, who do not want to receive email from you.
        """
        AbusePercent = None #double

        """
        Percent of Bounced users
        """
        FailedSpamPercent = None #double

        """
        Numeric reputation
        """
        Reputation = None #double

        """
        Amount of emails account can send daily
        """
        DailySendLimit = None #long

        """
        Name of account's status: Deleted, Disabled, UnderReview, NoPaymentsAllowed, NeverSignedIn, Active, SystemPaused
        """
        Status = None #string

        """
        Maximum size of email including attachments in MB's
        """
        EmailSizeLimit = None #int

        """
        Maximum number of contacts the account can have
        """
        MaxContacts = None #int

        """
        True, if you want to use Contact Delivery Tools.  Otherwise, false
        """
        EnableContactFeatures = None #bool

        """
        Sending permission setting for account
        """
        SendingPermission = None #ApiTypes.SendingPermission


    """
    Detailed account settings.
    """
    class SubAccountSettings:
        """
        Proper email address.
        """
        Email = None #string

        """
        True, if account needs credits to send emails. Otherwise, false
        """
        RequiresEmailCredits = None #bool

        """
        True, if account needs credits to buy templates. Otherwise, false
        """
        RequiresTemplateCredits = None #bool

        """
        Amount of credits added to account automatically
        """
        MonthlyRefillCredits = None #double

        """
        Amount of Litmus credits
        """
        LitmusCredits = None #decimal

        """
        True, if account is able to send template tests to Litmus. Otherwise, false
        """
        EnableLitmusTest = None #bool

        """
        True, if account needs credits to send emails. Otherwise, false
        """
        RequiresLitmusCredits = None #bool

        """
        Maximum size of email including attachments in MB's
        """
        EmailSizeLimit = None #int

        """
        Amount of emails account can send daily
        """
        DailySendLimit = None #int

        """
        Maximum number of contacts the account can have
        """
        MaxContacts = None #int

        """
        True, if account can request for private IP on its own. Otherwise, false
        """
        EnablePrivateIPRequest = None #bool

        """
        True, if you want to use Contact Delivery Tools.  Otherwise, false
        """
        EnableContactFeatures = None #bool

        """
        Sending permission setting for account
        """
        SendingPermission = None #ApiTypes.SendingPermission

        """
        Name of your custom IP Pool to be used in the sending process
        """
        PoolName = None #string

        """
        Public key for limited access to your account such as contact/add so you can use it safely on public websites.
        """
        PublicAccountID = None #string


    """
    A survey object
    """
    class Survey:
        """
        Survey identifier
        """
        PublicSurveyID = None #Guid

        """
        Creation date.
        """
        DateCreated = None #DateTime

        """
        Last change date
        """
        DateUpdated = None #DateTime?

        """
        
        """
        ExpiryDate = None #DateTime?

        """
        Filename
        """
        Name = None #string

        """
        Activate, delete, or pause your survey
        """
        Status = None #ApiTypes.SurveyStatus

        """
        Number of results count
        """
        ResultCount = None #int

        """
        
        """
        SurveySteps = None #List<ApiTypes.SurveyStep>

        """
        URL of the survey
        """
        SurveyLink = None #string


    """
    Object with the single answer's data
    """
    class SurveyResultAnswerInfo:
        """
        Answer's content
        """
        content = None #string

        """
        Identifier of the step
        """
        surveystepid = None #int

        """
        Identifier of the answer of the step
        """
        surveystepanswerid = None #string


    """
    Single answer's data with user's specific info
    """
    class SurveyResultInfo:
        """
        Identifier of the result
        """
        SurveyResultID = None #string

        """
        IP address
        """
        CreatedFromIP = None #string

        """
        Completion date
        """
        DateCompleted = None #DateTime

        """
        Start date
        """
        DateStart = None #DateTime

        """
        Answers for the survey
        """
        SurveyResultAnswers = None #List<ApiTypes.SurveyResultAnswerInfo>


    """
    
    """
    class SurveyResultsAnswer:
        """
        Identifier of the answer of the step
        """
        SurveyStepAnswerID = None #string

        """
        Number of items.
        """
        Count = None #int

        """
        Answer's content
        """
        Content = None #string


    """
    Data on the survey's result
    """
    class SurveyResultsSummaryInfo:
        """
        Number of items.
        """
        Count = None #int

        """
        Summary statistics
        """
        Summary = None #Dictionary<int, ApiTypes.List`1>


    """
    
    """
    class SurveyStatus(Enum):
        """
        The survey is deleted
        """
        Deleted = -1

        """
        The survey is not receiving result for now
        """
        Expired = 0

        """
        The survey is active and receiving answers
        """
        Active = 1


    """
    Survey's single step info with the answers
    """
    class SurveyStep:
        """
        Identifier of the step
        """
        SurveyStepID = None #int

        """
        Type of the step
        """
        SurveyStepType = None #ApiTypes.SurveyStepType

        """
        Type of the question
        """
        QuestionType = None #ApiTypes.QuestionType

        """
        Answer's content
        """
        Content = None #string

        """
        Is the answer required
        """
        Required = None #bool

        """
        Sequence of the answers
        """
        Sequence = None #int

        """
        
        """
        SurveyStepAnswers = None #List<ApiTypes.SurveyStepAnswer>


    """
    Single step's answer object
    """
    class SurveyStepAnswer:
        """
        Identifier of the answer of the step
        """
        SurveyStepAnswerID = None #string

        """
        Answer's content
        """
        Content = None #string

        """
        Sequence of the answers
        """
        Sequence = None #int


    """
    
    """
    class SurveyStepType(Enum):
        """
        
        """
        PageBreak = 1

        """
        
        """
        Question = 2

        """
        
        """
        TextMedia = 3

        """
        
        """
        ConfirmationPage = 4

        """
        
        """
        ExpiredPage = 5


    """
    Template
    """
    class Template:
        """
        ID number of template.
        """
        TemplateID = None #int

        """
        0 for API connections
        """
        TemplateType = None #ApiTypes.TemplateType

        """
        Filename
        """
        Name = None #string

        """
        Date of creation in YYYY-MM-DDThh:ii:ss format
        """
        DateAdded = None #DateTime

        """
        CSS style
        """
        Css = None #string

        """
        Default subject of email.
        """
        Subject = None #string

        """
        Default From: email address.
        """
        FromEmail = None #string

        """
        Default From: name.
        """
        FromName = None #string

        """
        HTML code of email (needs escaping).
        """
        BodyHtml = None #string

        """
        Text body of email.
        """
        BodyText = None #string

        """
        ID number of original template.
        """
        OriginalTemplateID = None #int

        """
        Enum: 0 - private, 1 - public, 2 - mockup
        """
        TemplateScope = None #ApiTypes.TemplateScope


    """
    List of templates (including drafts)
    """
    class TemplateList:
        """
        List of templates
        """
        Templates = None #List<ApiTypes.Template>

        """
        List of draft templates
        """
        DraftTemplate = None #List<ApiTypes.Template>


    """
    
    """
    class TemplateScope(Enum):
        """
        Template is available for this account only.
        """
        Private = 0

        """
        Template is available for this account and it's sub-accounts.
        """
        Public = 1


    """
    
    """
    class TemplateType(Enum):
        """
        Template supports any valid HTML
        """
        RawHTML = 0

        """
        Template is created and can only be modified in drag and drop editor
        """
        DragDropEditor = 1


    """
    Information about tracking link and its clicks.
    """
    class TrackedLink:
        """
        URL clicked
        """
        Link = None #string

        """
        Number of clicks
        """
        Clicks = None #string

        """
        Percent of clicks
        """
        Percent = None #string


    """
    
    """
    class TrackingType(Enum):
        """
        
        """
        EENone = -2

        """
        
        """
        Delete = -1

        """
        
        """
        Http = 0

        """
        
        """
        ExternalHttps = 1

        """
        
        """
        InternalCertHttps = 2

        """
        
        """
        LetsEncryptCert = 3


    """
    Status of ValidDomain used by DomainValidationService to determine how often tracking validation should be performed.
    """
    class TrackingValidationStatus(Enum):
        """
        
        """
        Validated = 0

        """
        
        """
        NotValidated = 1

        """
        
        """
        Invalid = 2

        """
        
        """
        Broken = 3


    """
    Account usage
    """
    class Usage:
        """
        Proper email address.
        """
        Email = None #string

        """
        True, if this account is a sub-account. Otherwise, false
        """
        IsSubAccount = None #bool

        """
        
        """
        List = None #List<ApiTypes.UsageData>


    """
    Detailed data about daily usage
    """
    class UsageData:
        """
        Date in YYYY-MM-DDThh:ii:ss format
        """
        Date = None #DateTime

        """
        Number of finished tasks
        """
        JobCount = None #int

        """
        Overall number of recipients
        """
        RecipientCount = None #int

        """
        Number of inbound emails
        """
        InboundCount = None #int

        """
        Number of attachments sent
        """
        AttachmentCount = None #int

        """
        Size of attachments sent
        """
        AttachmentsSize = None #long

        """
        Calculated cost of sending
        """
        Cost = None #decimal

        """
        Number of pricate IPs
        """
        PrivateIPCount = None #int?

        """
        
        """
        PrivateIPCost = None #decimal

        """
        Number of SMS
        """
        SmsCount = None #int?

        """
        Overall cost of SMS
        """
        SmsCost = None #decimal

        """
        Cost of templates
        """
        TemplateCost = None #decimal

        """
        Cost of email credits
        """
        EmailCreditsCost = None #int?

        """
        Cost of template credit
        """
        TemplateCreditsCost = None #int?

        """
        Cost of litmus credits
        """
        LitmusCost = None #decimal

        """
        Cost of 1 litmus credit
        """
        LitmusCreditsCost = None #decimal

        """
        Daily cost of Contact Delivery Tools
        """
        ContactCost = None #decimal

        """
        Number of contacts
        """
        ContactCount = None #long

        """
        
        """
        SupportCost = None #decimal

        """
        
        """
        EmailCost = None #decimal



""" 
Manage your AccessTokens (ApiKeys)
"""
class AccessToken:

    def Add(tokenName, accessLevel):
        """
        Add new AccessToken
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string tokenName - 
            ApiTypes.AccessLevel accessLevel - 
        Returns string
        """
        parameters = { 
                    'tokenName': tokenName,
                    'accessLevel': accessLevel.value}

        return ApiClient.Request('GET', '/accesstoken/add', parameters)

    def Delete(tokenName):
        """
        Permanently delete AccessToken.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string tokenName - 
        """
        parameters = { 
                    'tokenName': tokenName}

        return ApiClient.Request('GET', '/accesstoken/delete', parameters)

    def List():
        """
        Get AccessToken list.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.AccessToken>
        """

        return ApiClient.Request('GET', '/accesstoken/list', parameters)

    def Update(tokenName, accessLevel, tokenNameNew = None):
        """
        Edit AccessToken.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string tokenName - 
            ApiTypes.AccessLevel accessLevel - 
            string tokenNameNew -  (default None)
        """
        parameters = { 
                    'tokenName': tokenName,
                    'accessLevel': accessLevel.value,
                    'tokenNameNew': tokenNameNew}

        return ApiClient.Request('GET', '/accesstoken/update', parameters)


""" 
Methods for managing your account and subaccounts.
"""
class Account:

    def AddSubAccount(email, password, confirmPassword, requiresEmailCredits = False, enableLitmusTest = False, requiresLitmusCredits = False, maxContacts = 0, enablePrivateIPRequest = True, sendActivation = False, returnUrl = None, sendingPermission = None, enableContactFeatures = None, poolName = None, emailSizeLimit = 10, dailySendLimit = None):
        """
        Create new subaccount and provide most important data about it.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string email - Proper email address.
            string password - Current password.
            string confirmPassword - Repeat new password.
            bool requiresEmailCredits - True, if account needs credits to send emails. Otherwise, false (default False)
            bool enableLitmusTest - True, if account is able to send template tests to Litmus. Otherwise, false (default False)
            bool requiresLitmusCredits - True, if account needs credits to send emails. Otherwise, false (default False)
            int maxContacts - Maximum number of contacts the account can have (default 0)
            bool enablePrivateIPRequest - True, if account can request for private IP on its own. Otherwise, false (default True)
            bool sendActivation - True, if you want to send activation email to this account. Otherwise, false (default False)
            string returnUrl - URL to navigate to after account creation (default None)
            ApiTypes.SendingPermission? sendingPermission - Sending permission setting for account (default None)
            bool? enableContactFeatures - True, if you want to use Contact Delivery Tools.  Otherwise, false (default None)
            string poolName - Private IP required. Name of the custom IP Pool which Sub Account should use to send its emails. Leave empty for the default one or if no Private IPs have been bought (default None)
            int emailSizeLimit - Maximum size of email including attachments in MB's (default 10)
            int? dailySendLimit - Amount of emails account can send daily (default None)
        Returns string
        """
        parameters = { 
                    'email': email,
                    'password': password,
                    'confirmPassword': confirmPassword,
                    'requiresEmailCredits': requiresEmailCredits,
                    'enableLitmusTest': enableLitmusTest,
                    'requiresLitmusCredits': requiresLitmusCredits,
                    'maxContacts': maxContacts,
                    'enablePrivateIPRequest': enablePrivateIPRequest,
                    'sendActivation': sendActivation,
                    'returnUrl': returnUrl,
                    'sendingPermission': sendingPermission,
                    'enableContactFeatures': enableContactFeatures,
                    'poolName': poolName,
                    'emailSizeLimit': emailSizeLimit,
                    'dailySendLimit': dailySendLimit}

        return ApiClient.Request('GET', '/account/addsubaccount', parameters)

    def AddSubAccountCredits(credits, notes, creditType = ApiTypes.CreditType.Email, subAccountEmail = None, publicAccountID = None):
        """
        Add email, template or litmus credits to a sub-account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int credits - Amount of credits to add
            string notes - Specific notes about the transaction
            ApiTypes.CreditType creditType - Type of credits to add (Email or Litmus) (default ApiTypes.CreditType.Email)
            string subAccountEmail - Email address of sub-account (default None)
            string publicAccountID - Public key of sub-account to add credits to. Use subAccountEmail or publicAccountID not both. (default None)
        """
        parameters = { 
                    'credits': credits,
                    'notes': notes,
                    'creditType': creditType.value,
                    'subAccountEmail': subAccountEmail,
                    'publicAccountID': publicAccountID}

        return ApiClient.Request('GET', '/account/addsubaccountcredits', parameters)

    def ChangeEmail(newEmail, confirmEmail, sourceUrl = "https://elasticemail.com/account/"):
        """
        Change your email address. Remember, that your email address is used as login!
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string newEmail - New email address.
            string confirmEmail - New email address.
            string sourceUrl - URL from which request was sent. (default "https://elasticemail.com/account/")
        Returns string
        """
        parameters = { 
                    'newEmail': newEmail,
                    'confirmEmail': confirmEmail,
                    'sourceUrl': sourceUrl}

        return ApiClient.Request('GET', '/account/changeemail', parameters)

    def ChangePassword(newPassword, confirmPassword, currentPassword = None):
        """
        Create new password for your account. Password needs to be at least 6 characters long.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string newPassword - New password for account.
            string confirmPassword - Repeat new password.
            string currentPassword - Current password. (default None)
        """
        parameters = { 
                    'newPassword': newPassword,
                    'confirmPassword': confirmPassword,
                    'currentPassword': currentPassword}

        return ApiClient.Request('GET', '/account/changepassword', parameters)

    def DeleteSubAccount(subAccountEmail = None, publicAccountID = None):
        """
        Deletes specified Subaccount
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string subAccountEmail - Email address of sub-account (default None)
            string publicAccountID - Public key of sub-account to delete. Use subAccountEmail or publicAccountID not both. (default None)
        """
        parameters = { 
                    'subAccountEmail': subAccountEmail,
                    'publicAccountID': publicAccountID}

        return ApiClient.Request('GET', '/account/deletesubaccount', parameters)

    def GetSubAccountApiKey(subAccountEmail = None, publicAccountID = None):
        """
        Returns API Key for the given Sub Account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string subAccountEmail - Email address of sub-account (default None)
            string publicAccountID - Public key of sub-account to retrieve sub-account API Key. Use subAccountEmail or publicAccountID not both. (default None)
        Returns string
        """
        parameters = { 
                    'subAccountEmail': subAccountEmail,
                    'publicAccountID': publicAccountID}

        return ApiClient.Request('GET', '/account/getsubaccountapikey', parameters)

    def GetSubAccountList(limit = 0, offset = 0):
        """
        Lists all of your subaccounts
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int limit - Maximum of loaded items. (default 0)
            int offset - How many items should be loaded ahead. (default 0)
        Returns List<ApiTypes.SubAccount>
        """
        parameters = { 
                    'limit': limit,
                    'offset': offset}

        return ApiClient.Request('GET', '/account/getsubaccountlist', parameters)

    def Load():
        """
        Loads your account. Returns detailed information about your account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns ApiTypes.Account
        """

        return ApiClient.Request('GET', '/account/load', parameters)

    def LoadAdvancedOptions():
        """
        Load advanced options of your account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns ApiTypes.AdvancedOptions
        """

        return ApiClient.Request('GET', '/account/loadadvancedoptions', parameters)

    def LoadEmailCreditsHistory():
        """
        Lists email credits history
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.EmailCredits>
        """

        return ApiClient.Request('GET', '/account/loademailcreditshistory', parameters)

    def LoadInfo():
        """
        Loads your account. Returns detailed information about your account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns ApiTypes.Account
        """

        return ApiClient.Request('GET', '/account/loadinfo', parameters)

    def LoadLitmusCreditsHistory():
        """
        Lists litmus credits history
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.LitmusCredits>
        """

        return ApiClient.Request('GET', '/account/loadlitmuscreditshistory', parameters)

    def LoadNotificationQueue():
        """
        Shows queue of newest notifications - very useful when you want to check what happened with mails that were not received.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.NotificationQueue>
        """

        return ApiClient.Request('GET', '/account/loadnotificationqueue', parameters)

    def LoadPaymentHistory(limit, offset, fromDate, toDate):
        """
        Lists all payments
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int limit - Maximum of loaded items.
            int offset - How many items should be loaded ahead.
            DateTime fromDate - Starting date for search in YYYY-MM-DDThh:mm:ss format.
            DateTime toDate - Ending date for search in YYYY-MM-DDThh:mm:ss format.
        Returns List<ApiTypes.Payment>
        """
        parameters = { 
                    'limit': limit,
                    'offset': offset,
                    'fromDate': fromDate,
                    'toDate': toDate}

        return ApiClient.Request('GET', '/account/loadpaymenthistory', parameters)

    def LoadPayoutHistory():
        """
        Lists all referral payout history
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.Payment>
        """

        return ApiClient.Request('GET', '/account/loadpayouthistory', parameters)

    def LoadReferralDetails():
        """
        Shows information about your referral details
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns ApiTypes.Referral
        """

        return ApiClient.Request('GET', '/account/loadreferraldetails', parameters)

    def LoadReputationHistory(limit = 20, offset = 0):
        """
        Shows latest changes in your sending reputation
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int limit - Maximum of loaded items. (default 20)
            int offset - How many items should be loaded ahead. (default 0)
        Returns List<ApiTypes.ReputationHistory>
        """
        parameters = { 
                    'limit': limit,
                    'offset': offset}

        return ApiClient.Request('GET', '/account/loadreputationhistory', parameters)

    def LoadReputationImpact():
        """
        Shows detailed information about your actual reputation score
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns ApiTypes.ReputationDetail
        """

        return ApiClient.Request('GET', '/account/loadreputationimpact', parameters)

    def LoadSpamCheck(limit = 20, offset = 0):
        """
        Returns detailed spam check.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int limit - Maximum of loaded items. (default 20)
            int offset - How many items should be loaded ahead. (default 0)
        Returns List<ApiTypes.SpamCheck>
        """
        parameters = { 
                    'limit': limit,
                    'offset': offset}

        return ApiClient.Request('GET', '/account/loadspamcheck', parameters)

    def LoadSubAccountsEmailCreditsHistory(subAccountEmail = None, publicAccountID = None):
        """
        Lists email credits history for sub-account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string subAccountEmail - Email address of sub-account (default None)
            string publicAccountID - Public key of sub-account to list history for. Use subAccountEmail or publicAccountID not both. (default None)
        Returns List<ApiTypes.EmailCredits>
        """
        parameters = { 
                    'subAccountEmail': subAccountEmail,
                    'publicAccountID': publicAccountID}

        return ApiClient.Request('GET', '/account/loadsubaccountsemailcreditshistory', parameters)

    def LoadSubAccountSettings(subAccountEmail = None, publicAccountID = None):
        """
        Loads settings of subaccount
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string subAccountEmail - Email address of sub-account (default None)
            string publicAccountID - Public key of sub-account to load settings for. Use subAccountEmail or publicAccountID not both. (default None)
        Returns ApiTypes.SubAccountSettings
        """
        parameters = { 
                    'subAccountEmail': subAccountEmail,
                    'publicAccountID': publicAccountID}

        return ApiClient.Request('GET', '/account/loadsubaccountsettings', parameters)

    def LoadSubAccountsLitmusCreditsHistory(subAccountEmail = None, publicAccountID = None):
        """
        Lists litmus credits history for sub-account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string subAccountEmail - Email address of sub-account (default None)
            string publicAccountID - Public key of sub-account to list history for. Use subAccountEmail or publicAccountID not both. (default None)
        Returns List<ApiTypes.LitmusCredits>
        """
        parameters = { 
                    'subAccountEmail': subAccountEmail,
                    'publicAccountID': publicAccountID}

        return ApiClient.Request('GET', '/account/loadsubaccountslitmuscreditshistory', parameters)

    def LoadUsage(EEfrom, to):
        """
        Shows usage of your account in given time.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            DateTime from - Starting date for search in YYYY-MM-DDThh:mm:ss format.
            DateTime to - Ending date for search in YYYY-MM-DDThh:mm:ss format.
        Returns List<ApiTypes.Usage>
        """
        parameters = { 
                    'from': EEfrom,
                    'to': to}

        return ApiClient.Request('GET', '/account/loadusage', parameters)

    def Overview():
        """
        Shows summary for your account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns ApiTypes.AccountOverview
        """

        return ApiClient.Request('GET', '/account/overview', parameters)

    def ProfileOverview():
        """
        Shows you account's profile basic overview
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns ApiTypes.Profile
        """

        return ApiClient.Request('GET', '/account/profileoverview', parameters)

    def RemoveSubAccountCredits(creditType, notes, subAccountEmail = None, publicAccountID = None, credits = None, removeAll = False):
        """
        Remove email, template or litmus credits from a sub-account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            ApiTypes.CreditType creditType - Type of credits to add (Email or Litmus)
            string notes - Specific notes about the transaction
            string subAccountEmail - Email address of sub-account (default None)
            string publicAccountID - Public key of sub-account to remove credits from. Use subAccountEmail or publicAccountID not both. (default None)
            int? credits - Amount of credits to remove (default None)
            bool removeAll - Remove all credits of this type from sub-account (overrides credits if provided) (default False)
        """
        parameters = { 
                    'creditType': creditType.value,
                    'notes': notes,
                    'subAccountEmail': subAccountEmail,
                    'publicAccountID': publicAccountID,
                    'credits': credits,
                    'removeAll': removeAll}

        return ApiClient.Request('GET', '/account/removesubaccountcredits', parameters)

    def RequestNewApiKey():
        """
        Request a new default APIKey.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns string
        """

        return ApiClient.Request('GET', '/account/requestnewapikey', parameters)

    def RequestPremiumSupport():
        """
        Request premium support for your account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        """

        return ApiClient.Request('GET', '/account/requestpremiumsupport', parameters)

    def RequestPrivateIP(count, notes):
        """
        Request a private IP for your Account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int count - Number of items.
            string notes - Free form field of notes
        """
        parameters = { 
                    'count': count,
                    'notes': notes}

        return ApiClient.Request('GET', '/account/requestprivateip', parameters)

    def UpdateAdvancedOptions(enableClickTracking = None, enableLinkClickTracking = None, manageSubscriptions = None, manageSubscribedOnly = None, transactionalOnUnsubscribe = None, skipListUnsubscribe = None, autoTextFromHtml = None, allowCustomHeaders = None, bccEmail = None, contentTransferEncoding = None, emailNotificationForError = None, emailNotificationEmail = None, webNotificationUrl = None, webNotificationNotifyOncePerEmail = None, webNotificationForSent = None, webNotificationForOpened = None, webNotificationForClicked = None, webNotificationForUnsubscribed = None, webNotificationForAbuseReport = None, webNotificationForError = None, hubCallBackUrl = "", inboundDomain = None, inboundContactsOnly = None, lowCreditNotification = None, enableUITooltips = None, enableContactFeatures = None, notificationsEmails = None, unsubscribeNotificationsEmails = None, logoUrl = None, enableTemplateScripting = True, staleContactScore = None, staleContactInactiveDays = None, deliveryReason = None, tutorialsEnabled = None, enableOpenTracking = None, consentTrackingOnUnsubscribe = None):
        """
        Update sending and tracking options of your account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            bool? enableClickTracking - True, if you want to track clicks. Otherwise, false (default None)
            bool? enableLinkClickTracking - True, if you want to track by link tracking. Otherwise, false (default None)
            bool? manageSubscriptions - True, if you want to display your labels on your unsubscribe form. Otherwise, false (default None)
            bool? manageSubscribedOnly - True, if you want to only display labels that the contact is subscribed to on your unsubscribe form. Otherwise, false (default None)
            bool? transactionalOnUnsubscribe - True, if you want to display an option for the contact to opt into transactional email only on your unsubscribe form. Otherwise, false (default None)
            bool? skipListUnsubscribe - True, if you do not want to use list-unsubscribe headers. Otherwise, false (default None)
            bool? autoTextFromHtml - True, if text BODY of message should be created automatically. Otherwise, false (default None)
            bool? allowCustomHeaders - True, if you want to apply custom headers to your emails. Otherwise, false (default None)
            string bccEmail - Email address to send a copy of all email to. (default None)
            string contentTransferEncoding - Type of content encoding (default None)
            bool? emailNotificationForError - True, if you want bounce notifications returned. Otherwise, false (default None)
            string emailNotificationEmail - Specific email address to send bounce email notifications to. (default None)
            string webNotificationUrl - URL address to receive web notifications to parse and process. (default None)
            bool? webNotificationNotifyOncePerEmail - True, if you want to receive notifications for each type only once per email. Otherwise, false (default None)
            bool? webNotificationForSent - True, if you want to send web notifications for sent email. Otherwise, false (default None)
            bool? webNotificationForOpened - True, if you want to send web notifications for opened email. Otherwise, false (default None)
            bool? webNotificationForClicked - True, if you want to send web notifications for clicked email. Otherwise, false (default None)
            bool? webNotificationForUnsubscribed - True, if you want to send web notifications for unsubscribed email. Otherwise, false (default None)
            bool? webNotificationForAbuseReport - True, if you want to send web notifications for complaint email. Otherwise, false (default None)
            bool? webNotificationForError - True, if you want to send web notifications for bounced email. Otherwise, false (default None)
            string hubCallBackUrl - URL used for tracking action of inbound emails (default "")
            string inboundDomain - Domain you use as your inbound domain (default None)
            bool? inboundContactsOnly - True, if you want inbound email to only process contacts from your account. Otherwise, false (default None)
            bool? lowCreditNotification - True, if you want to receive low credit email notifications. Otherwise, false (default None)
            bool? enableUITooltips - True, if account has tooltips active. Otherwise, false (default None)
            bool? enableContactFeatures - True, if you want to use Contact Delivery Tools.  Otherwise, false (default None)
            string notificationsEmails - Email addresses to send a copy of all notifications from our system. Separated by semicolon (default None)
            string unsubscribeNotificationsEmails - Emails, separated by semicolon, to which the notification about contact unsubscribing should be sent to (default None)
            string logoUrl - URL to your logo image. (default None)
            bool? enableTemplateScripting - True, if you want to use template scripting in your emails {{}}. Otherwise, false (default True)
            int? staleContactScore - (0 means this functionality is NOT enabled) Score, depending on the number of times you have sent to a recipient, at which the given recipient should be moved to the Stale status (default None)
            int? staleContactInactiveDays - (0 means this functionality is NOT enabled) Number of days of inactivity for a contact after which the given recipient should be moved to the Stale status (default None)
            string deliveryReason - Why your clients are receiving your emails. (default None)
            bool? tutorialsEnabled - True, if you want to enable Dashboard Tutotials (default None)
            bool? enableOpenTracking - True, if you want to track opens. Otherwise, false (default None)
            bool? consentTrackingOnUnsubscribe -  (default None)
        Returns ApiTypes.AdvancedOptions
        """
        parameters = { 
                    'enableClickTracking': enableClickTracking,
                    'enableLinkClickTracking': enableLinkClickTracking,
                    'manageSubscriptions': manageSubscriptions,
                    'manageSubscribedOnly': manageSubscribedOnly,
                    'transactionalOnUnsubscribe': transactionalOnUnsubscribe,
                    'skipListUnsubscribe': skipListUnsubscribe,
                    'autoTextFromHtml': autoTextFromHtml,
                    'allowCustomHeaders': allowCustomHeaders,
                    'bccEmail': bccEmail,
                    'contentTransferEncoding': contentTransferEncoding,
                    'emailNotificationForError': emailNotificationForError,
                    'emailNotificationEmail': emailNotificationEmail,
                    'webNotificationUrl': webNotificationUrl,
                    'webNotificationNotifyOncePerEmail': webNotificationNotifyOncePerEmail,
                    'webNotificationForSent': webNotificationForSent,
                    'webNotificationForOpened': webNotificationForOpened,
                    'webNotificationForClicked': webNotificationForClicked,
                    'webNotificationForUnsubscribed': webNotificationForUnsubscribed,
                    'webNotificationForAbuseReport': webNotificationForAbuseReport,
                    'webNotificationForError': webNotificationForError,
                    'hubCallBackUrl': hubCallBackUrl,
                    'inboundDomain': inboundDomain,
                    'inboundContactsOnly': inboundContactsOnly,
                    'lowCreditNotification': lowCreditNotification,
                    'enableUITooltips': enableUITooltips,
                    'enableContactFeatures': enableContactFeatures,
                    'notificationsEmails': notificationsEmails,
                    'unsubscribeNotificationsEmails': unsubscribeNotificationsEmails,
                    'logoUrl': logoUrl,
                    'enableTemplateScripting': enableTemplateScripting,
                    'staleContactScore': staleContactScore,
                    'staleContactInactiveDays': staleContactInactiveDays,
                    'deliveryReason': deliveryReason,
                    'tutorialsEnabled': tutorialsEnabled,
                    'enableOpenTracking': enableOpenTracking,
                    'consentTrackingOnUnsubscribe': consentTrackingOnUnsubscribe}

        return ApiClient.Request('GET', '/account/updateadvancedoptions', parameters)

    def UpdateCustomBranding(enablePrivateBranding = False, logoUrl = None, supportLink = None, privateBrandingUrl = None, smtpAddress = None, smtpAlternative = None, paymentUrl = None):
        """
        Update settings of your private branding. These settings are needed, if you want to use Elastic Email under your brand.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            bool enablePrivateBranding - True: Turn on or off ability to send mails under your brand. Otherwise, false (default False)
            string logoUrl - URL to your logo image. (default None)
            string supportLink - Address to your support. (default None)
            string privateBrandingUrl - Subdomain for your rebranded service (default None)
            string smtpAddress - Address of SMTP server. (default None)
            string smtpAlternative - Address of alternative SMTP server. (default None)
            string paymentUrl - URL for making payments. (default None)
        """
        parameters = { 
                    'enablePrivateBranding': enablePrivateBranding,
                    'logoUrl': logoUrl,
                    'supportLink': supportLink,
                    'privateBrandingUrl': privateBrandingUrl,
                    'smtpAddress': smtpAddress,
                    'smtpAlternative': smtpAlternative,
                    'paymentUrl': paymentUrl}

        return ApiClient.Request('GET', '/account/updatecustombranding', parameters)

    def UpdateProfile(firstName, lastName, address1, city, state, zip, countryID, marketingConsent = None, address2 = None, company = None, website = None, logoUrl = None, taxCode = None, phone = None):
        """
        Update your profile.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string firstName - First name.
            string lastName - Last name.
            string address1 - First line of address.
            string city - City.
            string state - State or province.
            string zip - Zip/postal code.
            int countryID - Numeric ID of country. A file with the list of countries is available <a href="http://api.elasticemail.com/public/countries"><b>here</b></a>
            bool? marketingConsent - True if you want to receive newsletters from Elastic Email. Otherwise, false. Empty to leave the current value. (default None)
            string address2 - Second line of address. (default None)
            string company - Company name. (default None)
            string website - HTTP address of your website. (default None)
            string logoUrl - URL to your logo image. (default None)
            string taxCode - Code used for tax purposes. (default None)
            string phone - Phone number (default None)
        """
        parameters = { 
                    'firstName': firstName,
                    'lastName': lastName,
                    'address1': address1,
                    'city': city,
                    'state': state,
                    'zip': zip,
                    'countryID': countryID,
                    'marketingConsent': marketingConsent,
                    'address2': address2,
                    'company': company,
                    'website': website,
                    'logoUrl': logoUrl,
                    'taxCode': taxCode,
                    'phone': phone}

        return ApiClient.Request('GET', '/account/updateprofile', parameters)

    def UpdateSubAccountSettings(requiresEmailCredits = False, monthlyRefillCredits = 0, requiresLitmusCredits = False, enableLitmusTest = False, dailySendLimit = None, emailSizeLimit = 10, enablePrivateIPRequest = False, maxContacts = 0, subAccountEmail = None, publicAccountID = None, sendingPermission = None, enableContactFeatures = None, poolName = None):
        """
        Updates settings of specified subaccount
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            bool requiresEmailCredits - True, if account needs credits to send emails. Otherwise, false (default False)
            int monthlyRefillCredits - Amount of credits added to account automatically (default 0)
            bool requiresLitmusCredits - True, if account needs credits to send emails. Otherwise, false (default False)
            bool enableLitmusTest - True, if account is able to send template tests to Litmus. Otherwise, false (default False)
            int? dailySendLimit - Amount of emails account can send daily (default None)
            int emailSizeLimit - Maximum size of email including attachments in MB's (default 10)
            bool enablePrivateIPRequest - True, if account can request for private IP on its own. Otherwise, false (default False)
            int maxContacts - Maximum number of contacts the account can have (default 0)
            string subAccountEmail - Email address of sub-account (default None)
            string publicAccountID - Public key of sub-account to update. Use subAccountEmail or publicAccountID not both. (default None)
            ApiTypes.SendingPermission? sendingPermission - Sending permission setting for account (default None)
            bool? enableContactFeatures - True, if you want to use Contact Delivery Tools.  Otherwise, false (default None)
            string poolName - Name of your custom IP Pool to be used in the sending process (default None)
        """
        parameters = { 
                    'requiresEmailCredits': requiresEmailCredits,
                    'monthlyRefillCredits': monthlyRefillCredits,
                    'requiresLitmusCredits': requiresLitmusCredits,
                    'enableLitmusTest': enableLitmusTest,
                    'dailySendLimit': dailySendLimit,
                    'emailSizeLimit': emailSizeLimit,
                    'enablePrivateIPRequest': enablePrivateIPRequest,
                    'maxContacts': maxContacts,
                    'subAccountEmail': subAccountEmail,
                    'publicAccountID': publicAccountID,
                    'sendingPermission': sendingPermission,
                    'enableContactFeatures': enableContactFeatures,
                    'poolName': poolName}

        return ApiClient.Request('GET', '/account/updatesubaccountsettings', parameters)


""" 
Sending and monitoring progress of your Campaigns
"""
class Campaign:

    def Add(campaign):
        """
        Adds a campaign to the queue for processing based on the configuration
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            ApiTypes.Campaign campaign - Json representation of a campaign
        Returns int
        """
        parameters = { 
                    'campaign': campaign}

        return ApiClient.Request('GET', '/campaign/add', parameters)

    def Copy(channelID):
        """
        Copy selected campaign
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int channelID - ID number of selected Channel.
        Returns int
        """
        parameters = { 
                    'channelID': channelID}

        return ApiClient.Request('GET', '/campaign/copy', parameters)

    def Delete(channelID):
        """
        Delete selected campaign
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int channelID - ID number of selected Channel.
        """
        parameters = { 
                    'channelID': channelID}

        return ApiClient.Request('GET', '/campaign/delete', parameters)

    def Export(channelIDs = {}, fileFormat = ApiTypes.ExportFileFormats.Csv, compressionFormat = ApiTypes.CompressionFormat.EENone, fileName = None):
        """
        Export selected campaigns to chosen file format.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<int> channelIDs - List of campaign IDs used for processing (default None)
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
        Returns ApiTypes.ExportLink
        """
        parameters = { 
                    'channelIDs': ";".join(map(str, channelIDs)),
                    'fileFormat': fileFormat.value,
                    'compressionFormat': compressionFormat.value,
                    'fileName': fileName}

        return ApiClient.Request('GET', '/campaign/export', parameters)

    def List(search = None, offset = 0, limit = 0):
        """
        List all of your campaigns
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string search - Text fragment used for searching. (default None)
            int offset - How many items should be loaded ahead. (default 0)
            int limit - Maximum of loaded items. (default 0)
        Returns List<ApiTypes.CampaignChannel>
        """
        parameters = { 
                    'search': search,
                    'offset': offset,
                    'limit': limit}

        return ApiClient.Request('GET', '/campaign/list', parameters)

    def Update(campaign):
        """
        Updates a previously added campaign.  Only Active and Paused campaigns can be updated.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            ApiTypes.Campaign campaign - Json representation of a campaign
        Returns int
        """
        parameters = { 
                    'campaign': campaign}

        return ApiClient.Request('GET', '/campaign/update', parameters)


""" 
SMTP and HTTP API channels for grouping email delivery.
"""
class Channel:

    def Add(name):
        """
        Manually add a channel to your account to group email
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string name - Descriptive name of the channel
        Returns string
        """
        parameters = { 
                    'name': name}

        return ApiClient.Request('GET', '/channel/add', parameters)

    def Delete(name):
        """
        Delete the channel.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string name - The name of the channel to delete.
        """
        parameters = { 
                    'name': name}

        return ApiClient.Request('GET', '/channel/delete', parameters)

    def ExportCsv(channelNames, compressionFormat = ApiTypes.CompressionFormat.EENone, fileName = None):
        """
        Export channels in CSV file format.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<string> channelNames - List of channel names used for processing
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
        Returns File
        """
        parameters = { 
                    'channelNames': ";".join(map(str, channelNames)),
                    'compressionFormat': compressionFormat.value,
                    'fileName': fileName}

        return ApiClient.Request('GET', '/channel/exportcsv', parameters)

    def ExportJson(channelNames, compressionFormat = ApiTypes.CompressionFormat.EENone, fileName = None):
        """
        Export channels in JSON file format.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<string> channelNames - List of channel names used for processing
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
        Returns File
        """
        parameters = { 
                    'channelNames': ";".join(map(str, channelNames)),
                    'compressionFormat': compressionFormat.value,
                    'fileName': fileName}

        return ApiClient.Request('GET', '/channel/exportjson', parameters)

    def ExportXml(channelNames, compressionFormat = ApiTypes.CompressionFormat.EENone, fileName = None):
        """
        Export channels in XML file format.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<string> channelNames - List of channel names used for processing
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
        Returns File
        """
        parameters = { 
                    'channelNames': ";".join(map(str, channelNames)),
                    'compressionFormat': compressionFormat.value,
                    'fileName': fileName}

        return ApiClient.Request('GET', '/channel/exportxml', parameters)

    def List():
        """
        List all of your channels
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.Channel>
        """

        return ApiClient.Request('GET', '/channel/list', parameters)

    def Update(name, newName):
        """
        Rename an existing channel.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string name - The name of the channel to update.
            string newName - The new name for the channel.
        Returns string
        """
        parameters = { 
                    'name': name,
                    'newName': newName}

        return ApiClient.Request('GET', '/channel/update', parameters)


""" 
Methods used to manage your Contacts.
"""
class Contact:

    def Add(publicAccountID, email, publicListID = {}, listName = [], firstName = None, lastName = None, source = ApiTypes.ContactSource.ContactApi, returnUrl = None, sourceUrl = None, activationReturnUrl = None, activationTemplate = None, sendActivation = True, consentDate = None, consentIP = None, field = {}, notifyEmail = None, alreadyActiveUrl = None, consentTracking = ApiTypes.ConsentTracking.Unknown):
        """
        Add a new contact and optionally to one of your lists.  Note that your API KEY is not required for this call.
            string publicAccountID - Public key for limited access to your account such as contact/add so you can use it safely on public websites.
            string email - Proper email address.
            IEnumerable<string> publicListID - ID code of list (default None)
            string[] listName - Name of your list. (default None)
            string firstName - First name. (default None)
            string lastName - Last name. (default None)
            ApiTypes.ContactSource source - Specifies the way of uploading the contact (default ApiTypes.ContactSource.ContactApi)
            string returnUrl - URL to navigate to after account creation (default None)
            string sourceUrl - URL from which request was sent. (default None)
            string activationReturnUrl - The url to return the contact to after activation. (default None)
            string activationTemplate -  (default None)
            bool sendActivation - True, if you want to send activation email to this account. Otherwise, false (default True)
            DateTime? consentDate - Date of consent to send this contact(s) your email. If not provided current date is used for consent. (default None)
            string consentIP - IP address of consent to send this contact(s) your email. If not provided your current public IP address is used for consent. (default None)
            Dictionary<string, string> field - Custom contact field like firstname, lastname, city etc. Request parameters prefixed by field_ like field_firstname, field_lastname  (default None)
            string notifyEmail - Emails, separated by semicolon, to which the notification about contact subscribing should be sent to (default None)
            string alreadyActiveUrl -  (default None)
            ApiTypes.ConsentTracking consentTracking -  (default ApiTypes.ConsentTracking.Unknown)
        Returns string
        """
        parameters = { 
                    'publicAccountID': publicAccountID,
                    'email': email,
                    'publicListID': ";".join(map(str, publicListID)),
                    'listName': ";".join(map(str, listName)),
                    'firstName': firstName,
                    'lastName': lastName,
                    'source': source.value,
                    'returnUrl': returnUrl,
                    'sourceUrl': sourceUrl,
                    'activationReturnUrl': activationReturnUrl,
                    'activationTemplate': activationTemplate,
                    'sendActivation': sendActivation,
                    'consentDate': consentDate,
                    'consentIP': consentIP,
                    'notifyEmail': notifyEmail,
                    'alreadyActiveUrl': alreadyActiveUrl,
                    'consentTracking': consentTracking.value}
        ApiClient.AddDictionaryParameter(field, "field", parameters)

        return ApiClient.Request('GET', '/contact/add', parameters)

    def AddBlocked(email, status):
        """
        Manually add or update a contacts status to Abuse or Unsubscribed status (blocked).
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string email - Proper email address.
            ApiTypes.ContactStatus status - Name of status: Active, Engaged, Inactive, Abuse, Bounced, Unsubscribed.
        """
        parameters = { 
                    'email': email,
                    'status': status.value}

        return ApiClient.Request('GET', '/contact/addblocked', parameters)

    def ChangeProperty(email, name, value):
        """
        Change any property on the contact record.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string email - Proper email address.
            string name - Name of the contact property you want to change.
            string value - Value you would like to change the contact property to.
        """
        parameters = { 
                    'email': email,
                    'name': name,
                    'value': value}

        return ApiClient.Request('GET', '/contact/changeproperty', parameters)

    def ChangeStatus(status, rule = None, emails = {}):
        """
        Changes status of selected Contacts. You may provide RULE for selection or specify list of Contact IDs.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            ApiTypes.ContactStatus status - Name of status: Active, Engaged, Inactive, Abuse, Bounced, Unsubscribed.
            string rule - Query used for filtering. (default None)
            IEnumerable<string> emails - Comma delimited list of contact emails (default None)
        """
        parameters = { 
                    'status': status.value,
                    'rule': rule,
                    'emails': ";".join(map(str, emails))}

        return ApiClient.Request('GET', '/contact/changestatus', parameters)

    def CountByStatus(rule = None, allContacts = False):
        """
        Returns number of Contacts, RULE specifies contact Status.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string rule - Query used for filtering. (default None)
            bool allContacts - True: Include every Contact in your Account. Otherwise, false (default False)
        Returns ApiTypes.ContactStatusCounts
        """
        parameters = { 
                    'rule': rule,
                    'allContacts': allContacts}

        return ApiClient.Request('GET', '/contact/countbystatus', parameters)

    def CountByUnsubscribeReason(EEfrom = None, to = None):
        """
        Returns count of unsubscribe reasons for unsubscribed and complaint contacts.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            DateTime? from - Starting date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - Ending date for search in YYYY-MM-DDThh:mm:ss format. (default None)
        Returns ApiTypes.ContactUnsubscribeReasonCounts
        """
        parameters = { 
                    'from': EEfrom,
                    'to': to}

        return ApiClient.Request('GET', '/contact/countbyunsubscribereason', parameters)

    def Delete(rule = None, emails = {}):
        """
        Permanantly deletes the contacts provided.  You can provide either a qualified rule or a list of emails (comma separated string).
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string rule - Query used for filtering. (default None)
            IEnumerable<string> emails - Comma delimited list of contact emails (default None)
        """
        parameters = { 
                    'rule': rule,
                    'emails': ";".join(map(str, emails))}

        return ApiClient.Request('GET', '/contact/delete', parameters)

    def Export(fileFormat = ApiTypes.ExportFileFormats.Csv, rule = None, emails = {}, compressionFormat = ApiTypes.CompressionFormat.EENone, fileName = None):
        """
        Export selected Contacts to file.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            string rule - Query used for filtering. (default None)
            IEnumerable<string> emails - Comma delimited list of contact emails (default None)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
        Returns ApiTypes.ExportLink
        """
        parameters = { 
                    'fileFormat': fileFormat.value,
                    'rule': rule,
                    'emails': ";".join(map(str, emails)),
                    'compressionFormat': compressionFormat.value,
                    'fileName': fileName}

        return ApiClient.Request('GET', '/contact/export', parameters)

    def ExportUnsubscribeReasonCount(EEfrom = None, to = None, fileFormat = ApiTypes.ExportFileFormats.Csv, compressionFormat = ApiTypes.CompressionFormat.EENone, fileName = None):
        """
        Export contacts' unsubscribe reasons count to file.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            DateTime? from - Starting date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - Ending date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
        Returns ApiTypes.ExportLink
        """
        parameters = { 
                    'from': EEfrom,
                    'to': to,
                    'fileFormat': fileFormat.value,
                    'compressionFormat': compressionFormat.value,
                    'fileName': fileName}

        return ApiClient.Request('GET', '/contact/exportunsubscribereasoncount', parameters)

    def FindContact(email):
        """
        Finds all Lists and Segments this email belongs to.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string email - Proper email address.
        Returns ApiTypes.ContactCollection
        """
        parameters = { 
                    'email': email}

        return ApiClient.Request('GET', '/contact/findcontact', parameters)

    def GetContactsByList(listName, limit = 20, offset = 0):
        """
        List of Contacts for provided List
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
            int limit - Maximum of loaded items. (default 20)
            int offset - How many items should be loaded ahead. (default 0)
        Returns List<ApiTypes.Contact>
        """
        parameters = { 
                    'listName': listName,
                    'limit': limit,
                    'offset': offset}

        return ApiClient.Request('GET', '/contact/getcontactsbylist', parameters)

    def GetContactsBySegment(segmentName, limit = 20, offset = 0):
        """
        List of Contacts for provided Segment
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string segmentName - Name of your segment.
            int limit - Maximum of loaded items. (default 20)
            int offset - How many items should be loaded ahead. (default 0)
        Returns List<ApiTypes.Contact>
        """
        parameters = { 
                    'segmentName': segmentName,
                    'limit': limit,
                    'offset': offset}

        return ApiClient.Request('GET', '/contact/getcontactsbysegment', parameters)

    def List(rule = None, limit = 20, offset = 0):
        """
        List of all contacts. If you have not specified RULE, all Contacts will be listed.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string rule - Query used for filtering. (default None)
            int limit - Maximum of loaded items. (default 20)
            int offset - How many items should be loaded ahead. (default 0)
        Returns List<ApiTypes.Contact>
        """
        parameters = { 
                    'rule': rule,
                    'limit': limit,
                    'offset': offset}

        return ApiClient.Request('GET', '/contact/list', parameters)

    def LoadBlocked(statuses, search = None, limit = 0, offset = 0):
        """
        Load blocked contacts
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<ApiTypes.ContactStatus> statuses - List of blocked statuses: Abuse, Bounced or Unsubscribed
            string search - Text fragment used for searching. (default None)
            int limit - Maximum of loaded items. (default 0)
            int offset - How many items should be loaded ahead. (default 0)
        Returns List<ApiTypes.BlockedContact>
        """
        parameters = { 
                    'statuses': ";".join(map(str, statuses)),
                    'search': search,
                    'limit': limit,
                    'offset': offset}

        return ApiClient.Request('GET', '/contact/loadblocked', parameters)

    def LoadContact(email):
        """
        Load detailed contact information
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string email - Proper email address.
        Returns ApiTypes.Contact
        """
        parameters = { 
                    'email': email}

        return ApiClient.Request('GET', '/contact/loadcontact', parameters)

    def LoadHistory(email, limit = 0, offset = 0):
        """
        Shows detailed history of chosen Contact.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string email - Proper email address.
            int limit - Maximum of loaded items. (default 0)
            int offset - How many items should be loaded ahead. (default 0)
        Returns List<ApiTypes.ContactHistory>
        """
        parameters = { 
                    'email': email,
                    'limit': limit,
                    'offset': offset}

        return ApiClient.Request('GET', '/contact/loadhistory', parameters)

    def QuickAdd(emails, firstName = None, lastName = None, publicListID = None, listName = None, status = ApiTypes.ContactStatus.Active, notes = None, consentDate = None, consentIP = None, field = {}, notifyEmail = None, consentTracking = ApiTypes.ConsentTracking.Unknown):
        """
        Add new Contact to one of your Lists.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<string> emails - Comma delimited list of contact emails
            string firstName - First name. (default None)
            string lastName - Last name. (default None)
            string publicListID - ID code of list (default None)
            string listName - Name of your list. (default None)
            ApiTypes.ContactStatus status - Name of status: Active, Engaged, Inactive, Abuse, Bounced, Unsubscribed. (default ApiTypes.ContactStatus.Active)
            string notes - Free form field of notes (default None)
            DateTime? consentDate - Date of consent to send this contact(s) your email. If not provided current date is used for consent. (default None)
            string consentIP - IP address of consent to send this contact(s) your email. If not provided your current public IP address is used for consent. (default None)
            Dictionary<string, string> field - Custom contact field like firstname, lastname, city etc. Request parameters prefixed by field_ like field_firstname, field_lastname  (default None)
            string notifyEmail - Emails, separated by semicolon, to which the notification about contact subscribing should be sent to (default None)
            ApiTypes.ConsentTracking consentTracking -  (default ApiTypes.ConsentTracking.Unknown)
        """
        parameters = { 
                    'emails': ";".join(map(str, emails)),
                    'firstName': firstName,
                    'lastName': lastName,
                    'publicListID': publicListID,
                    'listName': listName,
                    'status': status.value,
                    'notes': notes,
                    'consentDate': consentDate,
                    'consentIP': consentIP,
                    'notifyEmail': notifyEmail,
                    'consentTracking': consentTracking.value}
        ApiClient.AddDictionaryParameter(field, "field", parameters)

        return ApiClient.Request('GET', '/contact/quickadd', parameters)

    def Subscribe(publicAccountID):
        """
        Basic double opt-in email subscribe form for your account.  This can be used for contacts that need to re-subscribe as well.
            string publicAccountID - Public key for limited access to your account such as contact/add so you can use it safely on public websites.
        Returns string
        """
        parameters = { 
                    'publicAccountID': publicAccountID}

        return ApiClient.Request('GET', '/contact/subscribe', parameters)

    def Update(email, firstName = None, lastName = None, clearRestOfFields = True, field = {}, customFields = None):
        """
        Update selected contact. Omitted contact's fields will be reset by default (see the clearRestOfFields parameter)
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string email - Proper email address.
            string firstName - First name. (default None)
            string lastName - Last name. (default None)
            bool clearRestOfFields - States if the fields that were omitted in this request are to be reset or should they be left with their current value (default True)
            Dictionary<string, string> field - Custom contact field like firstname, lastname, city etc. Request parameters prefixed by field_ like field_firstname, field_lastname  (default None)
            string customFields - Custom contact field like firstname, lastname, city etc. JSON serialized text like { "city":"london" }  (default None)
        Returns ApiTypes.Contact
        """
        parameters = { 
                    'email': email,
                    'firstName': firstName,
                    'lastName': lastName,
                    'clearRestOfFields': clearRestOfFields,
                    'customFields': customFields}
        ApiClient.AddDictionaryParameter(field, "field", parameters)

        return ApiClient.Request('GET', '/contact/update', parameters)

    def Upload(contactFile, allowUnsubscribe = False, listID = None, listName = None, status = ApiTypes.ContactStatus.Active, consentDate = None, consentIP = None, consentTracking = ApiTypes.ConsentTracking.Unknown):
        """
        Upload contacts in CSV file.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            File contactFile - Name of CSV file with Contacts.
            bool allowUnsubscribe - True: Allow unsubscribing from this (optional) newly created list. Otherwise, false (default False)
            int? listID - ID number of selected list. (default None)
            string listName - Name of your list to upload contacts to, or how the new, automatically created list should be named (default None)
            ApiTypes.ContactStatus status - Name of status: Active, Engaged, Inactive, Abuse, Bounced, Unsubscribed. (default ApiTypes.ContactStatus.Active)
            DateTime? consentDate - Date of consent to send this contact(s) your email. If not provided current date is used for consent. (default None)
            string consentIP - IP address of consent to send this contact(s) your email. If not provided your current public IP address is used for consent. (default None)
            ApiTypes.ConsentTracking consentTracking -  (default ApiTypes.ConsentTracking.Unknown)
        Returns int
        """
        attachments = []
        for name in contactFile:
            attachments.append(('attachments', open(name, 'rb')))

        parameters = { 
                    'allowUnsubscribe': allowUnsubscribe,
                    'listID': listID,
                    'listName': listName,
                    'status': status.value,
                    'consentDate': consentDate,
                    'consentIP': consentIP,
                    'consentTracking': consentTracking.value}

        return ApiClient.Request('POST', '/contact/upload', parameters, attachments)


""" 
Managing sender domains. Creating new entries and validating domain records.
"""
class Domain:

    def Add(domain, trackingType = ApiTypes.TrackingType.Http):
        """
        Add new domain to account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Name of selected domain.
            ApiTypes.TrackingType trackingType -  (default ApiTypes.TrackingType.Http)
        """
        parameters = { 
                    'domain': domain,
                    'trackingType': trackingType.value}

        return ApiClient.Request('GET', '/domain/add', parameters)

    def Delete(domain):
        """
        Deletes configured domain from account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Name of selected domain.
        """
        parameters = { 
                    'domain': domain}

        return ApiClient.Request('GET', '/domain/delete', parameters)

    def List():
        """
        Lists all domains configured for this account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.DomainDetail>
        """

        return ApiClient.Request('GET', '/domain/list', parameters)

    def SetDefault(domain):
        """
        Verification of email addres set for domain.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Default email sender, example: mail@yourdomain.com
        """
        parameters = { 
                    'domain': domain}

        return ApiClient.Request('GET', '/domain/setdefault', parameters)

    def VerifyDkim(domain):
        """
        Verification of DKIM record for domain
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Name of selected domain.
        Returns string
        """
        parameters = { 
                    'domain': domain}

        return ApiClient.Request('GET', '/domain/verifydkim', parameters)

    def VerifyMX(domain):
        """
        Verification of MX record for domain
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Name of selected domain.
        Returns string
        """
        parameters = { 
                    'domain': domain}

        return ApiClient.Request('GET', '/domain/verifymx', parameters)

    def VerifySpf(domain):
        """
        Verification of SPF record for domain
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Name of selected domain.
        Returns string
        """
        parameters = { 
                    'domain': domain}

        return ApiClient.Request('GET', '/domain/verifyspf', parameters)

    def VerifyTracking(domain, trackingType = ApiTypes.TrackingType.Http):
        """
        Verification of tracking CNAME record for domain
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Name of selected domain.
            ApiTypes.TrackingType trackingType -  (default ApiTypes.TrackingType.Http)
        Returns string
        """
        parameters = { 
                    'domain': domain,
                    'trackingType': trackingType.value}

        return ApiClient.Request('GET', '/domain/verifytracking', parameters)


""" 

"""
class Email:

    def GetStatus(transactionID, showFailed = False, showSent = False, showDelivered = False, showPending = False, showOpened = False, showClicked = False, showAbuse = False, showUnsubscribed = False, showErrors = False, showMessageIDs = False):
        """
        Get email batch status
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string transactionID - Transaction identifier
            bool showFailed - Include Bounced email addresses. (default False)
            bool showSent - Include Sent email addresses. (default False)
            bool showDelivered - Include all delivered email addresses. (default False)
            bool showPending - Include Ready to send email addresses. (default False)
            bool showOpened - Include Opened email addresses. (default False)
            bool showClicked - Include Clicked email addresses. (default False)
            bool showAbuse - Include Reported as abuse email addresses. (default False)
            bool showUnsubscribed - Include Unsubscribed email addresses. (default False)
            bool showErrors - Include error messages for bounced emails. (default False)
            bool showMessageIDs - Include all MessageIDs for this transaction (default False)
        Returns ApiTypes.EmailJobStatus
        """
        parameters = { 
                    'transactionID': transactionID,
                    'showFailed': showFailed,
                    'showSent': showSent,
                    'showDelivered': showDelivered,
                    'showPending': showPending,
                    'showOpened': showOpened,
                    'showClicked': showClicked,
                    'showAbuse': showAbuse,
                    'showUnsubscribed': showUnsubscribed,
                    'showErrors': showErrors,
                    'showMessageIDs': showMessageIDs}

        return ApiClient.Request('GET', '/email/getstatus', parameters)

    def Send(subject = None, EEfrom = None, fromName = None, sender = None, senderName = None, msgFrom = None, msgFromName = None, replyTo = None, replyToName = None, to = {}, msgTo = {}, msgCC = {}, msgBcc = {}, lists = {}, segments = {}, mergeSourceFilename = None, dataSource = None, channel = None, bodyHtml = None, bodyText = None, charset = None, charsetBodyHtml = None, charsetBodyText = None, encodingType = ApiTypes.EncodingType.EENone, template = None, attachmentFiles = {}, headers = {}, postBack = None, merge = {}, timeOffSetMinutes = None, poolName = None, isTransactional = False, attachments = {}, trackOpens = None, trackClicks = None):
        """
        Submit emails. The HTTP POST request is suggested. The default, maximum (accepted by us) size of an email is 10 MB in total, with or without attachments included. For suggested implementations please refer to https://elasticemail.com/support/http-api/
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string subject - Email subject (default None)
            string from - From email address (default None)
            string fromName - Display name for from email address (default None)
            string sender - Email address of the sender (default None)
            string senderName - Display name sender (default None)
            string msgFrom - Optional parameter. Sets FROM MIME header. (default None)
            string msgFromName - Optional parameter. Sets FROM name of MIME header. (default None)
            string replyTo - Email address to reply to (default None)
            string replyToName - Display name of the reply to address (default None)
            IEnumerable<string> to - List of email recipients (each email is treated separately, like a BCC). Separated by comma or semicolon. We suggest using the "msgTo" parameter if backward compatibility with API version 1 is not a must. (default None)
            IEnumerable<string> msgTo - Optional parameter. Will be ignored if the 'to' parameter is also provided. List of email recipients (visible to all other recipients of the message as TO MIME header). Separated by comma or semicolon. (default None)
            IEnumerable<string> msgCC - Optional parameter. Will be ignored if the 'to' parameter is also provided. List of email recipients (visible to all other recipients of the message as CC MIME header). Separated by comma or semicolon. (default None)
            IEnumerable<string> msgBcc - Optional parameter. Will be ignored if the 'to' parameter is also provided. List of email recipients (each email is treated seperately). Separated by comma or semicolon. (default None)
            IEnumerable<string> lists - The name of a contact list you would like to send to. Separate multiple contact lists by commas or semicolons. (default None)
            IEnumerable<string> segments - The name of a segment you would like to send to. Separate multiple segments by comma or semicolon. Insert "0" for all Active contacts. (default None)
            string mergeSourceFilename - File name one of attachments which is a CSV list of Recipients. (default None)
            string dataSource - Name or ID of the previously uploaded file which should be a CSV list of Recipients. (default None)
            string channel - An ID field (max 191 chars) that can be used for reporting [will default to HTTP API or SMTP API] (default None)
            string bodyHtml - Html email body (default None)
            string bodyText - Text email body (default None)
            string charset - Text value of charset encoding for example: iso-8859-1, windows-1251, utf-8, us-ascii, windows-1250 and more… (default None)
            string charsetBodyHtml - Sets charset for body html MIME part (overrides default value from charset parameter) (default None)
            string charsetBodyText - Sets charset for body text MIME part (overrides default value from charset parameter) (default None)
            ApiTypes.EncodingType encodingType - 0 for None, 1 for Raw7Bit, 2 for Raw8Bit, 3 for QuotedPrintable, 4 for Base64 (Default), 5 for Uue  note that you can also provide the text version such as "Raw7Bit" for value 1.  NOTE: Base64 or QuotedPrintable is recommended if you are validating your domain(s) with DKIM. (default ApiTypes.EncodingType.EENone)
            string template - The ID of an email template you have created in your account. (default None)
            IEnumerableFile attachmentFiles - Attachment files. These files should be provided with the POST multipart file upload, not directly in the request's URL. Can also include merge CSV file (default None)
            Dictionary<string, string> headers - Optional Custom Headers. Request parameters prefixed by headers_ like headers_customheader1, headers_customheader2. Note: a space is required after the colon before the custom header value. headers_xmailer=xmailer: header-value1 (default None)
            string postBack - Optional header returned in notifications. (default None)
            Dictionary<string, string> merge - Request parameters prefixed by merge_ like merge_firstname, merge_lastname. If sending to a template you can send merge_ fields to merge data with the template. Template fields are entered with {firstname}, {lastname} etc. (default None)
            string timeOffSetMinutes - Number of minutes in the future this email should be sent up to a maximum of 1 year (524160 minutes) (default None)
            string poolName - Name of your custom IP Pool to be used in the sending process (default None)
            bool isTransactional - True, if email is transactional (non-bulk, non-marketing, non-commercial). Otherwise, false (default False)
            IEnumerable<string> attachments - Names or IDs of attachments previously uploaded to your account that should be sent with this e-mail. (default None)
            bool? trackOpens - Should the opens be tracked? If no value has been provided, account's default setting will be used. (default None)
            bool? trackClicks - Should the clicks be tracked? If no value has been provided, account's default setting will be used. (default None)
        Returns ApiTypes.EmailSend
        """
        attachments = []
        for name in attachmentFiles:
            attachments.append(('attachments', open(name, 'rb')))

        parameters = { 
                    'subject': subject,
                    'from': EEfrom,
                    'fromName': fromName,
                    'sender': sender,
                    'senderName': senderName,
                    'msgFrom': msgFrom,
                    'msgFromName': msgFromName,
                    'replyTo': replyTo,
                    'replyToName': replyToName,
                    'to': ";".join(map(str, to)),
                    'msgTo': ";".join(map(str, msgTo)),
                    'msgCC': ";".join(map(str, msgCC)),
                    'msgBcc': ";".join(map(str, msgBcc)),
                    'lists': ";".join(map(str, lists)),
                    'segments': ";".join(map(str, segments)),
                    'mergeSourceFilename': mergeSourceFilename,
                    'dataSource': dataSource,
                    'channel': channel,
                    'bodyHtml': bodyHtml,
                    'bodyText': bodyText,
                    'charset': charset,
                    'charsetBodyHtml': charsetBodyHtml,
                    'charsetBodyText': charsetBodyText,
                    'encodingType': encodingType.value,
                    'template': template,
                    'postBack': postBack,
                    'timeOffSetMinutes': timeOffSetMinutes,
                    'poolName': poolName,
                    'isTransactional': isTransactional,
                    'attachments': ";".join(map(str, attachments)),
                    'trackOpens': trackOpens,
                    'trackClicks': trackClicks}
        ApiClient.AddDictionaryParameter(headers, "headers", parameters)
        ApiClient.AddDictionaryParameter(merge, "merge", parameters)

        return ApiClient.Request('POST', '/email/send', parameters, attachments)

    def Status(messageID):
        """
        Detailed status of a unique email sent through your account. Returns a 'Email has expired and the status is unknown.' error, if the email has not been fully processed yet.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string messageID - Unique identifier for this email.
        Returns ApiTypes.EmailStatus
        """
        parameters = { 
                    'messageID': messageID}

        return ApiClient.Request('GET', '/email/status', parameters)

    def View(messageID):
        """
        View email
            string messageID - Message identifier
        Returns ApiTypes.EmailView
        """
        parameters = { 
                    'messageID': messageID}

        return ApiClient.Request('GET', '/email/view', parameters)


""" 

"""
class Export:

    def CheckStatus(publicExportID):
        """
        Check the current status of the export.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            Guid publicExportID - 
        Returns ApiTypes.ExportStatus
        """
        parameters = { 
                    'publicExportID': publicExportID}

        return ApiClient.Request('GET', '/export/checkstatus', parameters)

    def CountByType():
        """
        Summary of export type counts.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns ApiTypes.ExportTypeCounts
        """

        return ApiClient.Request('GET', '/export/countbytype', parameters)

    def Delete(publicExportID):
        """
        Delete the specified export.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            Guid publicExportID - 
        """
        parameters = { 
                    'publicExportID': publicExportID}

        return ApiClient.Request('GET', '/export/delete', parameters)

    def List(limit = 0, offset = 0):
        """
        Returns a list of all exported data.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int limit - Maximum of loaded items. (default 0)
            int offset - How many items should be loaded ahead. (default 0)
        Returns List<ApiTypes.Export>
        """
        parameters = { 
                    'limit': limit,
                    'offset': offset}

        return ApiClient.Request('GET', '/export/list', parameters)


""" 
Manage the files on your account
"""
class File:

    def Delete(fileID = None, filename = None):
        """
        Permanently deletes the file from your account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int? fileID -  (default None)
            string filename - Name of your file. (default None)
        """
        parameters = { 
                    'fileID': fileID,
                    'filename': filename}

        return ApiClient.Request('GET', '/file/delete', parameters)

    def Download(filename = None, fileID = None):
        """
        Gets content of the chosen File
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string filename - Name of your file. (default None)
            int? fileID -  (default None)
        Returns File
        """
        parameters = { 
                    'filename': filename,
                    'fileID': fileID}

        return ApiClient.Request('GET', '/file/download', parameters)

    def List(msgID):
        """
        Lists your available Attachments in the given email
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string msgID - ID number of selected message.
        Returns List<ApiTypes.File>
        """
        parameters = { 
                    'msgID': msgID}

        return ApiClient.Request('GET', '/file/list', parameters)

    def ListAll():
        """
        Lists all your available files
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.File>
        """

        return ApiClient.Request('GET', '/file/listall', parameters)

    def Load(filename):
        """
        Gets chosen File
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string filename - Name of your file.
        Returns ApiTypes.File
        """
        parameters = { 
                    'filename': filename}

        return ApiClient.Request('GET', '/file/load', parameters)

    def Upload(file, name = None, expiresAfterDays = 35):
        """
        Uploads selected file to the server using http form upload format (MIME multipart/form-data) or PUT method.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            File file - 
            string name - Filename (default None)
            int? expiresAfterDays - After how many days should the file be deleted. (default 35)
        Returns ApiTypes.File
        """
        attachments = []
        for name in file:
            attachments.append(('attachments', open(name, 'rb')))

        parameters = { 
                    'name': name,
                    'expiresAfterDays': expiresAfterDays}

        return ApiClient.Request('POST', '/file/upload', parameters, attachments)


""" 
API methods for managing your Lists
"""
class List:

    def Add(listName, createEmptyList = False, allowUnsubscribe = False, rule = None, emails = {}, allContacts = False):
        """
        Create new list, based on filtering rule or list of IDs
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
            bool createEmptyList - True to create an empty list, otherwise false. Ignores rule and emails parameters if provided. (default False)
            bool allowUnsubscribe - True: Allow unsubscribing from this list. Otherwise, false (default False)
            string rule - Query used for filtering. (default None)
            IEnumerable<string> emails - Comma delimited list of contact emails (default None)
            bool allContacts - True: Include every Contact in your Account. Otherwise, false (default False)
        Returns int
        """
        parameters = { 
                    'listName': listName,
                    'createEmptyList': createEmptyList,
                    'allowUnsubscribe': allowUnsubscribe,
                    'rule': rule,
                    'emails': ";".join(map(str, emails)),
                    'allContacts': allContacts}

        return ApiClient.Request('GET', '/list/add', parameters)

    def AddContacts(listName, rule = None, emails = {}, allContacts = False):
        """
        Add existing Contacts to chosen list
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
            string rule - Query used for filtering. (default None)
            IEnumerable<string> emails - Comma delimited list of contact emails (default None)
            bool allContacts - True: Include every Contact in your Account. Otherwise, false (default False)
        """
        parameters = { 
                    'listName': listName,
                    'rule': rule,
                    'emails': ";".join(map(str, emails)),
                    'allContacts': allContacts}

        return ApiClient.Request('GET', '/list/addcontacts', parameters)

    def Copy(sourceListName, newlistName = None, createEmptyList = None, allowUnsubscribe = None, rule = None):
        """
        Copy your existing List with the option to provide new settings to it. Some fields, when left empty, default to the source list's settings
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string sourceListName - The name of the list you want to copy
            string newlistName - Name of your list if you want to change it. (default None)
            bool? createEmptyList - True to create an empty list, otherwise false. Ignores rule and emails parameters if provided. (default None)
            bool? allowUnsubscribe - True: Allow unsubscribing from this list. Otherwise, false (default None)
            string rule - Query used for filtering. (default None)
        Returns int
        """
        parameters = { 
                    'sourceListName': sourceListName,
                    'newlistName': newlistName,
                    'createEmptyList': createEmptyList,
                    'allowUnsubscribe': allowUnsubscribe,
                    'rule': rule}

        return ApiClient.Request('GET', '/list/copy', parameters)

    def CreateFromCampaign(campaignID, listName, statuses = {}):
        """
        Create a new list from the recipients of the given campaign, using the given statuses of Messages
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int campaignID - ID of the campaign which recipients you want to copy
            string listName - Name of your list.
            IEnumerable<ApiTypes.LogJobStatus> statuses - Statuses of a campaign's emails you want to include in the new list (but NOT the contacts' statuses) (default None)
        Returns int
        """
        parameters = { 
                    'campaignID': campaignID,
                    'listName': listName,
                    'statuses': ";".join(map(str, statuses))}

        return ApiClient.Request('GET', '/list/createfromcampaign', parameters)

    def CreateNthSelectionLists(listName, numberOfLists, excludeBlocked = True, allowUnsubscribe = False, rule = None, allContacts = False):
        """
        Create a series of nth selection lists from an existing list or segment
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
            int numberOfLists - The number of evenly distributed lists to create.
            bool excludeBlocked - True if you want to exclude contacts that are currently in a blocked status of either unsubscribe, complaint or bounce. Otherwise, false. (default True)
            bool allowUnsubscribe - True: Allow unsubscribing from this list. Otherwise, false (default False)
            string rule - Query used for filtering. (default None)
            bool allContacts - True: Include every Contact in your Account. Otherwise, false (default False)
        """
        parameters = { 
                    'listName': listName,
                    'numberOfLists': numberOfLists,
                    'excludeBlocked': excludeBlocked,
                    'allowUnsubscribe': allowUnsubscribe,
                    'rule': rule,
                    'allContacts': allContacts}

        return ApiClient.Request('GET', '/list/createnthselectionlists', parameters)

    def CreateRandomList(listName, count, excludeBlocked = True, allowUnsubscribe = False, rule = None, allContacts = False):
        """
        Create a new list with randomized contacts from an existing list or segment
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
            int count - Number of items.
            bool excludeBlocked - True if you want to exclude contacts that are currently in a blocked status of either unsubscribe, complaint or bounce. Otherwise, false. (default True)
            bool allowUnsubscribe - True: Allow unsubscribing from this list. Otherwise, false (default False)
            string rule - Query used for filtering. (default None)
            bool allContacts - True: Include every Contact in your Account. Otherwise, false (default False)
        Returns int
        """
        parameters = { 
                    'listName': listName,
                    'count': count,
                    'excludeBlocked': excludeBlocked,
                    'allowUnsubscribe': allowUnsubscribe,
                    'rule': rule,
                    'allContacts': allContacts}

        return ApiClient.Request('GET', '/list/createrandomlist', parameters)

    def Delete(listName):
        """
        Deletes List and removes all the Contacts from it (does not delete Contacts).
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
        """
        parameters = { 
                    'listName': listName}

        return ApiClient.Request('GET', '/list/delete', parameters)

    def Export(listName, fileFormat = ApiTypes.ExportFileFormats.Csv, compressionFormat = ApiTypes.CompressionFormat.EENone, fileName = None):
        """
        Exports all the contacts from the provided list
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
        Returns ApiTypes.ExportLink
        """
        parameters = { 
                    'listName': listName,
                    'fileFormat': fileFormat.value,
                    'compressionFormat': compressionFormat.value,
                    'fileName': fileName}

        return ApiClient.Request('GET', '/list/export', parameters)

    def list(EEfrom = None, to = None):
        """
        Shows all your existing lists
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            DateTime? from - Starting date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - Ending date for search in YYYY-MM-DDThh:mm:ss format. (default None)
        Returns List<ApiTypes.List>
        """
        parameters = { 
                    'from': EEfrom,
                    'to': to}

        return ApiClient.Request('GET', '/list/list', parameters)

    def Load(listName):
        """
        Returns detailed information about specific list.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
        Returns ApiTypes.List
        """
        parameters = { 
                    'listName': listName}

        return ApiClient.Request('GET', '/list/load', parameters)

    def MoveContacts(oldListName, newListName, emails = {}, moveAll = None, statuses = {}, rule = None):
        """
        Move selected contacts from one List to another
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string oldListName - The name of the list from which the contacts will be copied from
            string newListName - The name of the list to copy the contacts to
            IEnumerable<string> emails - Comma delimited list of contact emails (default None)
            bool? moveAll - TRUE - moves all contacts; FALSE - moves contacts provided in the 'emails' parameter. This is ignored if the 'statuses' parameter has been provided (default None)
            IEnumerable<ApiTypes.ContactStatus> statuses - List of contact statuses which are eligible to move. This ignores the 'moveAll' parameter (default None)
            string rule - Query used for filtering. (default None)
        """
        parameters = { 
                    'oldListName': oldListName,
                    'newListName': newListName,
                    'emails': ";".join(map(str, emails)),
                    'moveAll': moveAll,
                    'statuses': ";".join(map(str, statuses)),
                    'rule': rule}

        return ApiClient.Request('GET', '/list/movecontacts', parameters)

    def RemoveContacts(listName, rule = None, emails = {}):
        """
        Remove selected Contacts from your list
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
            string rule - Query used for filtering. (default None)
            IEnumerable<string> emails - Comma delimited list of contact emails (default None)
        """
        parameters = { 
                    'listName': listName,
                    'rule': rule,
                    'emails': ";".join(map(str, emails))}

        return ApiClient.Request('GET', '/list/removecontacts', parameters)

    def Update(listName, newListName = None, allowUnsubscribe = False):
        """
        Update existing list
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string listName - Name of your list.
            string newListName - Name of your list if you want to change it. (default None)
            bool allowUnsubscribe - True: Allow unsubscribing from this list. Otherwise, false (default False)
        """
        parameters = { 
                    'listName': listName,
                    'newListName': newListName,
                    'allowUnsubscribe': allowUnsubscribe}

        return ApiClient.Request('GET', '/list/update', parameters)


""" 
Methods to check logs of your campaigns
"""
class Log:

    def CancelInProgress(channelName = None, transactionID = None):
        """
        Cancels emails that are waiting to be sent.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string channelName - Name of selected channel. (default None)
            string transactionID - ID number of transaction (default None)
        """
        parameters = { 
                    'channelName': channelName,
                    'transactionID': transactionID}

        return ApiClient.Request('GET', '/log/cancelinprogress', parameters)

    def Export(statuses, fileFormat = ApiTypes.ExportFileFormats.Csv, EEfrom = None, to = None, channelName = None, includeEmail = True, includeSms = True, messageCategory = {}, compressionFormat = ApiTypes.CompressionFormat.EENone, fileName = None, email = None):
        """
        Export email log information to the specified file format.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<ApiTypes.LogJobStatus> statuses - List of comma separated message statuses: 0 for all, 1 for ReadyToSend, 2 for InProgress, 4 for Bounced, 5 for Sent, 6 for Opened, 7 for Clicked, 8 for Unsubscribed, 9 for Abuse Report
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            DateTime? from - Start date. (default None)
            DateTime? to - End date. (default None)
            string channelName - Name of selected channel. (default None)
            bool includeEmail - True: Search includes emails. Otherwise, false. (default True)
            bool includeSms - True: Search includes SMS. Otherwise, false. (default True)
            IEnumerable<ApiTypes.MessageCategory> messageCategory - ID of message category (default None)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
            string email - Proper email address. (default None)
        Returns ApiTypes.ExportLink
        """
        parameters = { 
                    'statuses': ";".join(map(str, statuses)),
                    'fileFormat': fileFormat.value,
                    'from': EEfrom,
                    'to': to,
                    'channelName': channelName,
                    'includeEmail': includeEmail,
                    'includeSms': includeSms,
                    'messageCategory': ";".join(map(str, messageCategory)),
                    'compressionFormat': compressionFormat.value,
                    'fileName': fileName,
                    'email': email}

        return ApiClient.Request('GET', '/log/export', parameters)

    def ExportLinkTracking(EEfrom, to, channelName = None, fileFormat = ApiTypes.ExportFileFormats.Csv, limit = 0, offset = 0, compressionFormat = ApiTypes.CompressionFormat.EENone, fileName = None):
        """
        Export detailed link tracking information to the specified file format.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            DateTime? from - Starting date for search in YYYY-MM-DDThh:mm:ss format.
            DateTime? to - Ending date for search in YYYY-MM-DDThh:mm:ss format.
            string channelName - Name of selected channel. (default None)
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            int limit - Maximum of loaded items. (default 0)
            int offset - How many items should be loaded ahead. (default 0)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
        Returns ApiTypes.ExportLink
        """
        parameters = { 
                    'from': EEfrom,
                    'to': to,
                    'channelName': channelName,
                    'fileFormat': fileFormat.value,
                    'limit': limit,
                    'offset': offset,
                    'compressionFormat': compressionFormat.value,
                    'fileName': fileName}

        return ApiClient.Request('GET', '/log/exportlinktracking', parameters)

    def LinkTracking(EEfrom = None, to = None, limit = 0, offset = 0, channelName = None):
        """
        Track link clicks
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            DateTime? from - Starting date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - Ending date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            int limit - Maximum of loaded items. (default 0)
            int offset - How many items should be loaded ahead. (default 0)
            string channelName - Name of selected channel. (default None)
        Returns ApiTypes.LinkTrackingDetails
        """
        parameters = { 
                    'from': EEfrom,
                    'to': to,
                    'limit': limit,
                    'offset': offset,
                    'channelName': channelName}

        return ApiClient.Request('GET', '/log/linktracking', parameters)

    def Load(statuses, EEfrom = None, to = None, channelName = None, limit = 0, offset = 0, includeEmail = True, includeSms = True, messageCategory = {}, email = None, useStatusChangeDate = False):
        """
        Returns logs filtered by specified parameters.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<ApiTypes.LogJobStatus> statuses - List of comma separated message statuses: 0 for all, 1 for ReadyToSend, 2 for InProgress, 4 for Bounced, 5 for Sent, 6 for Opened, 7 for Clicked, 8 for Unsubscribed, 9 for Abuse Report
            DateTime? from - Starting date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - Ending date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            string channelName - Name of selected channel. (default None)
            int limit - Maximum of loaded items. (default 0)
            int offset - How many items should be loaded ahead. (default 0)
            bool includeEmail - True: Search includes emails. Otherwise, false. (default True)
            bool includeSms - True: Search includes SMS. Otherwise, false. (default True)
            IEnumerable<ApiTypes.MessageCategory> messageCategory - ID of message category (default None)
            string email - Proper email address. (default None)
            bool useStatusChangeDate - True, if 'from' and 'to' parameters should resolve to the Status Change date. To resolve to the creation date - false (default False)
        Returns ApiTypes.Log
        """
        parameters = { 
                    'statuses': ";".join(map(str, statuses)),
                    'from': EEfrom,
                    'to': to,
                    'channelName': channelName,
                    'limit': limit,
                    'offset': offset,
                    'includeEmail': includeEmail,
                    'includeSms': includeSms,
                    'messageCategory': ";".join(map(str, messageCategory)),
                    'email': email,
                    'useStatusChangeDate': useStatusChangeDate}

        return ApiClient.Request('GET', '/log/load', parameters)

    def LoadNotifications(statuses, EEfrom = None, to = None, limit = 0, offset = 0, messageCategory = {}, useStatusChangeDate = False, notificationType = ApiTypes.NotificationType.All):
        """
        Returns notification logs filtered by specified parameters.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<ApiTypes.LogJobStatus> statuses - List of comma separated message statuses: 0 for all, 1 for ReadyToSend, 2 for InProgress, 4 for Bounced, 5 for Sent, 6 for Opened, 7 for Clicked, 8 for Unsubscribed, 9 for Abuse Report
            DateTime? from - Starting date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - Ending date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            int limit - Maximum of loaded items. (default 0)
            int offset - How many items should be loaded ahead. (default 0)
            IEnumerable<ApiTypes.MessageCategory> messageCategory - ID of message category (default None)
            bool useStatusChangeDate - True, if 'from' and 'to' parameters should resolve to the Status Change date. To resolve to the creation date - false (default False)
            ApiTypes.NotificationType notificationType -  (default ApiTypes.NotificationType.All)
        Returns ApiTypes.Log
        """
        parameters = { 
                    'statuses': ";".join(map(str, statuses)),
                    'from': EEfrom,
                    'to': to,
                    'limit': limit,
                    'offset': offset,
                    'messageCategory': ";".join(map(str, messageCategory)),
                    'useStatusChangeDate': useStatusChangeDate,
                    'notificationType': notificationType.value}

        return ApiClient.Request('GET', '/log/loadnotifications', parameters)

    def RetryNow(msgID):
        """
        Retry sending of temporarily not delivered message.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string msgID - ID number of selected message.
        """
        parameters = { 
                    'msgID': msgID}

        return ApiClient.Request('GET', '/log/retrynow', parameters)

    def Summary(EEfrom, to, channelName = None, interval = ApiTypes.IntervalType.Summary, transactionID = None):
        """
        Loads summary information about activity in chosen date range.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            DateTime from - Starting date for search in YYYY-MM-DDThh:mm:ss format.
            DateTime to - Ending date for search in YYYY-MM-DDThh:mm:ss format.
            string channelName - Name of selected channel. (default None)
            ApiTypes.IntervalType interval - 'Hourly' for detailed information, 'summary' for daily overview (default ApiTypes.IntervalType.Summary)
            string transactionID - ID number of transaction (default None)
        Returns ApiTypes.LogSummary
        """
        parameters = { 
                    'from': EEfrom,
                    'to': to,
                    'channelName': channelName,
                    'interval': interval.value,
                    'transactionID': transactionID}

        return ApiClient.Request('GET', '/log/summary', parameters)


""" 
Manages your segments - dynamically created lists of contacts
"""
class Segment:

    def Add(segmentName, rule):
        """
        Create new segment, based on specified RULE.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string segmentName - Name of your segment.
            string rule - Query used for filtering.
        Returns ApiTypes.Segment
        """
        parameters = { 
                    'segmentName': segmentName,
                    'rule': rule}

        return ApiClient.Request('GET', '/segment/add', parameters)

    def Copy(sourceSegmentName, newSegmentName = None, rule = None):
        """
        Copy your existing Segment with the optional new rule and custom name
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string sourceSegmentName - The name of the segment you want to copy
            string newSegmentName - New name of your segment if you want to change it. (default None)
            string rule - Query used for filtering. (default None)
        Returns ApiTypes.Segment
        """
        parameters = { 
                    'sourceSegmentName': sourceSegmentName,
                    'newSegmentName': newSegmentName,
                    'rule': rule}

        return ApiClient.Request('GET', '/segment/copy', parameters)

    def Delete(segmentName):
        """
        Delete existing segment.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string segmentName - Name of your segment.
        """
        parameters = { 
                    'segmentName': segmentName}

        return ApiClient.Request('GET', '/segment/delete', parameters)

    def Export(segmentName, fileFormat = ApiTypes.ExportFileFormats.Csv, compressionFormat = ApiTypes.CompressionFormat.EENone, fileName = None):
        """
        Exports all the contacts from the provided segment
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string segmentName - Name of your segment.
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file. (default None)
        Returns ApiTypes.ExportLink
        """
        parameters = { 
                    'segmentName': segmentName,
                    'fileFormat': fileFormat.value,
                    'compressionFormat': compressionFormat.value,
                    'fileName': fileName}

        return ApiClient.Request('GET', '/segment/export', parameters)

    def List(includeHistory = False, EEfrom = None, to = None):
        """
        Lists all your available Segments
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            bool includeHistory - True: Include history of last 30 days. Otherwise, false. (default False)
            DateTime? from - From what date should the segment history be shown. In YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - To what date should the segment history be shown. In YYYY-MM-DDThh:mm:ss format. (default None)
        Returns List<ApiTypes.Segment>
        """
        parameters = { 
                    'includeHistory': includeHistory,
                    'from': EEfrom,
                    'to': to}

        return ApiClient.Request('GET', '/segment/list', parameters)

    def LoadByName(segmentNames, includeHistory = False, EEfrom = None, to = None):
        """
        Lists your available Segments using the provided names
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<string> segmentNames - Names of segments you want to load. Will load all contacts if left empty or the 'All Contacts' name has been provided
            bool includeHistory - True: Include history of last 30 days. Otherwise, false. (default False)
            DateTime? from - From what date should the segment history be shown. In YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - To what date should the segment history be shown. In YYYY-MM-DDThh:mm:ss format. (default None)
        Returns List<ApiTypes.Segment>
        """
        parameters = { 
                    'segmentNames': ";".join(map(str, segmentNames)),
                    'includeHistory': includeHistory,
                    'from': EEfrom,
                    'to': to}

        return ApiClient.Request('GET', '/segment/loadbyname', parameters)

    def Update(segmentName, newSegmentName = None, rule = None):
        """
        Rename or change RULE for your segment
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string segmentName - Name of your segment.
            string newSegmentName - New name of your segment if you want to change it. (default None)
            string rule - Query used for filtering. (default None)
        Returns ApiTypes.Segment
        """
        parameters = { 
                    'segmentName': segmentName,
                    'newSegmentName': newSegmentName,
                    'rule': rule}

        return ApiClient.Request('GET', '/segment/update', parameters)


""" 
Managing texting to your clients.
"""
class SMS:

    def Send(to, body):
        """
        Send a short SMS Message (maximum of 1600 characters) to any mobile phone.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string to - Mobile number you want to message. Can be any valid mobile number in E.164 format. To provide the country code you need to provide "+" before the number.  If your URL is not encoded then you need to replace the "+" with "%2B" instead.
            string body - Body of your message. The maximum body length is 160 characters.  If the message body is greater than 160 characters it is split into multiple messages and you are charged per message for the number of message required to send your length
        """
        parameters = { 
                    'to': to,
                    'body': body}

        return ApiClient.Request('GET', '/sms/send', parameters)


""" 
Methods to organize and get results of your surveys
"""
class Survey:

    def Add(survey):
        """
        Adds a new survey
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            ApiTypes.Survey survey - Json representation of a survey
        Returns ApiTypes.Survey
        """
        parameters = { 
                    'survey': survey}

        return ApiClient.Request('GET', '/survey/add', parameters)

    def Delete(publicSurveyID):
        """
        Deletes the survey
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            Guid publicSurveyID - Survey identifier
        """
        parameters = { 
                    'publicSurveyID': publicSurveyID}

        return ApiClient.Request('GET', '/survey/delete', parameters)

    def Export(publicSurveyID, fileName, fileFormat = ApiTypes.ExportFileFormats.Csv, compressionFormat = ApiTypes.CompressionFormat.EENone):
        """
        Export given survey's data to provided format
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            Guid publicSurveyID - Survey identifier
            string fileName - Name of your file.
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
        Returns ApiTypes.ExportLink
        """
        parameters = { 
                    'publicSurveyID': publicSurveyID,
                    'fileName': fileName,
                    'fileFormat': fileFormat.value,
                    'compressionFormat': compressionFormat.value}

        return ApiClient.Request('GET', '/survey/export', parameters)

    def List():
        """
        Shows all your existing surveys
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.Survey>
        """

        return ApiClient.Request('GET', '/survey/list', parameters)

    def LoadResponseList(publicSurveyID):
        """
        Get list of personal answers for the specific survey
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            Guid publicSurveyID - Survey identifier
        Returns List<ApiTypes.SurveyResultInfo>
        """
        parameters = { 
                    'publicSurveyID': publicSurveyID}

        return ApiClient.Request('GET', '/survey/loadresponselist', parameters)

    def LoadResults(publicSurveyID):
        """
        Get general results of the specific survey
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            Guid publicSurveyID - Survey identifier
        Returns ApiTypes.SurveyResultsSummaryInfo
        """
        parameters = { 
                    'publicSurveyID': publicSurveyID}

        return ApiClient.Request('GET', '/survey/loadresults', parameters)

    def Update(survey):
        """
        Update the survey information
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            ApiTypes.Survey survey - Json representation of a survey
        Returns ApiTypes.Survey
        """
        parameters = { 
                    'survey': survey}

        return ApiClient.Request('GET', '/survey/update', parameters)


""" 
Managing and editing templates of your emails
"""
class Template:

    def Add(name, subject, fromEmail, fromName, templateType = ApiTypes.TemplateType.RawHTML, templateScope = ApiTypes.TemplateScope.Private, bodyHtml = None, bodyText = None, css = None, originalTemplateID = 0):
        """
        Create new Template. Needs to be sent using POST method
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string name - Filename
            string subject - Default subject of email.
            string fromEmail - Default From: email address.
            string fromName - Default From: name.
            ApiTypes.TemplateType templateType - 0 for API connections (default ApiTypes.TemplateType.RawHTML)
            ApiTypes.TemplateScope templateScope - Enum: 0 - private, 1 - public, 2 - mockup (default ApiTypes.TemplateScope.Private)
            string bodyHtml - HTML code of email (needs escaping). (default None)
            string bodyText - Text body of email. (default None)
            string css - CSS style (default None)
            int originalTemplateID - ID number of original template. (default 0)
        Returns int
        """
        parameters = { 
                    'name': name,
                    'subject': subject,
                    'fromEmail': fromEmail,
                    'fromName': fromName,
                    'templateType': templateType.value,
                    'templateScope': templateScope.value,
                    'bodyHtml': bodyHtml,
                    'bodyText': bodyText,
                    'css': css,
                    'originalTemplateID': originalTemplateID}

        return ApiClient.Request('GET', '/template/add', parameters)

    def CheckUsage(templateID):
        """
        Check if template is used by campaign.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int templateID - ID number of template.
        Returns bool
        """
        parameters = { 
                    'templateID': templateID}

        return ApiClient.Request('GET', '/template/checkusage', parameters)

    def Copy(templateID, name, subject, fromEmail, fromName):
        """
        Copy Selected Template
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int templateID - ID number of template.
            string name - Filename
            string subject - Default subject of email.
            string fromEmail - Default From: email address.
            string fromName - Default From: name.
        Returns ApiTypes.Template
        """
        parameters = { 
                    'templateID': templateID,
                    'name': name,
                    'subject': subject,
                    'fromEmail': fromEmail,
                    'fromName': fromName}

        return ApiClient.Request('GET', '/template/copy', parameters)

    def Delete(templateID):
        """
        Delete template with the specified ID
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int templateID - ID number of template.
        """
        parameters = { 
                    'templateID': templateID}

        return ApiClient.Request('GET', '/template/delete', parameters)

    def GetEmbeddedHtml(templateID):
        """
        Search for references to images and replaces them with base64 code.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int templateID - ID number of template.
        Returns string
        """
        parameters = { 
                    'templateID': templateID}

        return ApiClient.Request('GET', '/template/getembeddedhtml', parameters)

    def GetList(limit = 500, offset = 0):
        """
        Lists your templates
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int limit - Maximum of loaded items. (default 500)
            int offset - How many items should be loaded ahead. (default 0)
        Returns ApiTypes.TemplateList
        """
        parameters = { 
                    'limit': limit,
                    'offset': offset}

        return ApiClient.Request('GET', '/template/getlist', parameters)

    def LoadTemplate(templateID, ispublic = False):
        """
        Load template with content
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int templateID - ID number of template.
            bool ispublic -  (default False)
        Returns ApiTypes.Template
        """
        parameters = { 
                    'templateID': templateID,
                    'ispublic': ispublic}

        return ApiClient.Request('GET', '/template/loadtemplate', parameters)

    def RemoveScreenshot(templateID):
        """
        Removes previously generated screenshot of template
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int templateID - ID number of template.
        """
        parameters = { 
                    'templateID': templateID}

        return ApiClient.Request('GET', '/template/removescreenshot', parameters)

    def SaveScreenshot(base64Image, templateID):
        """
        Saves screenshot of chosen Template
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string base64Image - Image, base64 coded.
            int templateID - ID number of template.
        Returns string
        """
        parameters = { 
                    'base64Image': base64Image,
                    'templateID': templateID}

        return ApiClient.Request('GET', '/template/savescreenshot', parameters)

    def Update(templateID, templateScope = ApiTypes.TemplateScope.Private, name = None, subject = None, fromEmail = None, fromName = None, bodyHtml = None, bodyText = None, css = None, removeScreenshot = True):
        """
        Update existing template, overwriting existing data. Needs to be sent using POST method.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int templateID - ID number of template.
            ApiTypes.TemplateScope templateScope - Enum: 0 - private, 1 - public, 2 - mockup (default ApiTypes.TemplateScope.Private)
            string name - Filename (default None)
            string subject - Default subject of email. (default None)
            string fromEmail - Default From: email address. (default None)
            string fromName - Default From: name. (default None)
            string bodyHtml - HTML code of email (needs escaping). (default None)
            string bodyText - Text body of email. (default None)
            string css - CSS style (default None)
            bool removeScreenshot -  (default True)
        """
        parameters = { 
                    'templateID': templateID,
                    'templateScope': templateScope.value,
                    'name': name,
                    'subject': subject,
                    'fromEmail': fromEmail,
                    'fromName': fromName,
                    'bodyHtml': bodyHtml,
                    'bodyText': bodyText,
                    'css': css,
                    'removeScreenshot': removeScreenshot}

        return ApiClient.Request('GET', '/template/update', parameters)

