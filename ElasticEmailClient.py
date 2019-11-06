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
			result = requests.post(ApiClient.apiUri + url, data = data, files = attachs)
		elif method == 'PUT':
			result = requests.put(ApiClient.apiUri + url, data = data)
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
        ViewAutomations = 64

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
        ModifyAutomations = 1048576

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
        ViewSupport = 8589934592

        """
        
        """
        SendHttp = 17179869184

        """
        
        """
        Modify2FA = 34359738368

        """
        
        """
        ModifySupport = 68719476736

        """
        
        """
        ViewCustomFields = 137438953472

        """
        
        """
        ModifyCustomFields = 274877906944

        """
        
        """
        ModifyWebNotifications = 549755813888

        """
        
        """
        ExtendedLogs = 1099511627776

        """
        
        """
        VerifyEmails = 2199023255552


    """
    
    """
    class AccessToken:
        """
        Access level or permission to be assigned to this Access Token.
        """
        AccessLevel = None #ApiTypes.AccessLevel

        """
        Filename
        """
        Name = None #string

        """
        Date this AccessToken was last used.
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
        
        """
        PublicAccountID = None #string

        """
        ApiKey that gives you access to our SMTP and HTTP API's.
        """
        ApiKey = None #string

        """
        True, if Account is a Sub-Account. Otherwise, false
        """
        IsSub = None #bool

        """
        
        """
        IsUser = None #bool

        """
        The number of Sub-Accounts this Account has.
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
        Amount of emails sent from this Account
        """
        TotalEmailsSent = None #long

        """
        Amount of emails sent from this Account
        """
        MonthlyEmailsSent = None #long?

        """
        Current credit in Account for Pay as you go plans. 
        """
        Credit = None #decimal

        """
        Amount of email credits
        """
        EmailCredits = None #int

        """
        Amount of emails sent from this Account
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
        Amount of emails Account can send daily
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
        
        """
        UntrustedDeviceAlertDisabled = None #bool


    """
    Basic overview of your account
    """
    class AccountOverview:
        """
        Amount of emails sent from this Account
        """
        TotalEmailsSent = None #long

        """
        Current credit in Account for Pay as you go plans. 
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
        Number of created Sub-Accounts
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
        True, if you want to receive low credit email notifications. Otherwise, false
        """
        LowCreditNotification = None #bool

        """
        True, if this Account is a Sub-Account. Otherwise, false
        """
        IsSubAccount = None #bool

        """
        True, if this Account resells Elastic Email. Otherwise, false.
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
        True, if Account has tooltips active. Otherwise, false
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
        True, if you want to enable Dashboard Tutotials
        """
        TutorialsEnabled = None #bool?


    """
    Blocked Contact - Contact returning Hard Bounces
    """
    class BlockedContact:
        """
        Proper email address.
        """
        Email = None #string

        """
        Status of the given resource
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
        Which Channel's event should trigger this Campaign
        """
        TriggerChannelID = None #int?

        """
        
        """
        TriggerChannelName = None #string

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
        Should the opens be tracked? If no value has been provided, Account's default setting will be used.
        """
        TrackOpens = None #bool?

        """
        Should the clicks be tracked? If no value has been provided, Account's default setting will be used.
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
        Date of last activity on Account
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
        
        """
        ParentChannelName = None #string

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
        Which Channel's event should trigger this Campaign
        """
        TriggerChannelID = None #int

        """
        
        """
        TriggerChannelName = None #string

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
        Name of template.
        """
        TemplateName = None #string

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
        Should the opens be tracked? If no value has been provided, Account's default setting will be used.
        """
        TrackOpens = None #bool?

        """
        Should the clicks be tracked? If no value has been provided, Account's default setting will be used.
        """
        TrackClicks = None #bool?

        """
        The utm_source marketing parameter appended to each link in the campaign.
        """
        UtmSource = None #string

        """
        The utm_medium marketing parameter appended to each link in the campaign.
        """
        UtmMedium = None #string

        """
        The utm_campaign marketing parameter appended to each link in the campaign.
        """
        UtmCampaign = None #string

        """
        The utm_content marketing parameter appended to each link in the campaign.
        """
        UtmContent = None #string


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
        
        """
        CampaignTemplateID = None #int?

        """
        
        """
        CampaignTemplateName = None #string

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
        Name of template.
        """
        TemplateName = None #string

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
        The utm_source marketing parameter appended to each link in the campaign.
        """
        UtmSource = None #string

        """
        The utm_medium marketing parameter appended to each link in the campaign.
        """
        UtmMedium = None #string

        """
        The utm_campaign marketing parameter appended to each link in the campaign.
        """
        UtmCampaign = None #string

        """
        The utm_content marketing parameter appended to each link in the campaign.
        """
        UtmContent = None #string


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
        Channel identifier.
        """
        ChannelID = None #int

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
        Status of the given resource
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
        
        """
        BounceCount = None #int

        """
        Custom contact field like companyname, customernumber, city etc. JSON serialized text like { "city":"london" } 
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
    class ContactSort(Enum):
        """
        
        """
        Unknown = 0

        """
        Sort by date added ascending order
        """
        DateAddedAsc = 1

        """
        Sort by date added descending order
        """
        DateAddedDesc = 2

        """
        Sort by date updated ascending order
        """
        DateUpdatedAsc = 3

        """
        Sort by date updated descending order
        """
        DateUpdatedDesc = 4


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
        Contact was added via the verification api.
        """
        VerificationApi = 5

        """
        Contacts were added via bulk verification api.
        """
        FileVerificationApi = 6


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
    Daily summary of log status, based on specified date range.
    """
    class DailyLogStatusSummary:
        """
        Date in YYYY-MM-DDThh:ii:ss format
        """
        Date = None #DateTime

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
        0 - Validated successfully, 1 - NotValidated , 2 - Invalid, 3 - Broken (tracking was frequnetly verfied in given period and still is invalid). For statuses: 0, 1, 3 tracking will be verified in normal periods. For status 2 tracking will be verified in high frequent periods.
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
        
        """
        VERP = None #bool

        """
        
        """
        CustomBouncesDomain = None #string

        """
        
        """
        IsCustomBouncesDomainDefault = None #bool


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
    
    """
    class EmailValidationResult:
        """
        
        """
        Account = None #string

        """
        Name of selected domain.
        """
        Domain = None #string

        """
        Proper email address.
        """
        Email = None #string

        """
        
        """
        SuggestedSpelling = None #string

        """
        
        """
        Disposable = None #bool

        """
        
        """
        Role = None #bool

        """
        Reason for blocking (1 - bounced, 2 - unsubscribed, 3 - spam).
        """
        Reason = None #string

        """
        
        """
        Result = None #ApiTypes.EmailValidationStatus


    """
    
    """
    class EmailValidationStatus(Enum):
        """
        
        """
        EENone = 0

        """
        
        """
        Valid = 1

        """
        
        """
        Unknown = 2

        """
        
        """
        Risky = 3

        """
        
        """
        Invalid = 4


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
    Event logs for selected date range
    """
    class EventLog:
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
        Recipients = None #List<ApiTypes.RecipientEvent>


    """
    Record of exported data from the system.
    """
    class Export:
        """
        ID of the exported file
        """
        PublicExportID = None #Guid

        """
        Date the export was created.
        """
        DateAdded = None #DateTime

        """
        Type of export
        """
        ExportType = None #ApiTypes.ExportType

        """
        Status of the export
        """
        ExportStatus = None #ApiTypes.ExportStatus

        """
        Long description of the export.
        """
        Info = None #string

        """
        Name of the exported file.
        """
        Filename = None #string

        """
        Link to download the export.
        """
        Link = None #string

        """
        Log start date (for Type = Log only).
        """
        LogFrom = None #DateTime?

        """
        Log end date (for Type = Log only).
        """
        LogTo = None #DateTime?


    """
    Format of the exported file.
    """
    class ExportFileFormats(Enum):
        """
        Export in comma separated values format.
        """
        Csv = 1

        """
        Export in xml format.
        """
        Xml = 2

        """
        Export in json format.
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
        ID of the exported file
        """
        PublicExportID = None #Guid


    """
    Current status of the export.
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
    Type of export.
    """
    class ExportType(Enum):
        """
        Export contains detailed email log information.
        """
        Log = 1

        """
        Export contains detailed contact information.
        """
        Contact = 2

        """
        Export contains detailed campaign information.
        """
        Campaign = 3

        """
        Export contains detailed link tracking information.
        """
        LinkTracking = 4

        """
        Export contains detailed survey information.
        """
        Survey = 5


    """
    
    """
    class File:
        """
        Name of your file including extension.
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
        Date when the file be deleted from your Account.
        """
        ExpirationDate = None #DateTime?

        """
        Content type of the file.
        """
        ContentType = None #string


    """
    Lists inbound options of your account.
    """
    class InboundOptions:
        """
        URL used for tracking action of inbound emails
        """
        HubCallbackUrl = None #string

        """
        Domain you use as your inbound domain
        """
        InboundDomain = None #string

        """
        True, if you want inbound email to only process contacts from your Account. Otherwise, false
        """
        InboundContactsOnly = None #bool


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
    class LogEventStatus(Enum):
        """
        Email is queued for sending.
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
        From = None #DateTime

        """
        Ending date for search in YYYY-MM-DDThh:mm:ss format.
        """
        To = None #DateTime

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
        SubaccountSummary = None #ApiTypes.SubaccountSummary


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
        
        """
        RegularAmount = None #decimal

        """
        
        """
        DiscountPercent = None #decimal

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
        Why your clients are receiving your emails.
        """
        DeliveryReason = None #string

        """
        True if you want to receive newsletters from Elastic Email. Otherwise, false. Empty to leave the current value.
        """
        MarketingConsent = None #bool?

        """
        HTTP address of your website.
        """
        Website = None #string

        """
        URL to your logo image.
        """
        LogoUrl = None #string


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
        MessageCategoryID = None #ApiTypes.MessageCategory?

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
        
        """
        EnvelopeFrom = None #string

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
        
        """
        IPAddress = None #string


    """
    Detailed information about message recipient
    """
    class RecipientEvent:
        """
        ID of certain mail job
        """
        JobID = None #string

        """
        ID number of selected message.
        """
        MsgID = None #string

        """
        Default From: email address.
        """
        FromEmail = None #string

        """
        Ending date for search in YYYY-MM-DDThh:mm:ss format.
        """
        To = None #string

        """
        Default subject of email.
        """
        Subject = None #string

        """
        Name of recipient's status: Submitted, ReadyToSend, WaitingToRetry, Sending, Bounced, Sent, Opened, Clicked, Unsubscribed, AbuseReport
        """
        EventType = None #string

        """
        Creation date
        """
        EventDate = None #string

        """
        Name of selected Channel.
        """
        Channel = None #string

        """
        ID number of selected Channel.
        """
        ChannelID = None #int?

        """
        Name of message category
        """
        MessageCategory = None #string

        """
        Date of next try
        """
        NextTryOn = None #string

        """
        Content of message, HTML encoded
        """
        Message = None #string

        """
        
        """
        IPAddress = None #string

        """
        
        """
        IPPoolName = None #string


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
        Points from proper setup of your Account
        """
        SetupScore = None #double

        """
        Number of emails included in the current reputation score.
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
    Controls the Sub-Account's sending permissions.  Main Account's always have All.
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
    Detailed information about Sub-Account.
    """
    class SubAccount:
        """
        
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
        Date of last activity on Account
        """
        LastActivity = None #string

        """
        Amount of email credits
        """
        EmailCredits = None #string

        """
        True, if Account needs credits to send emails. Otherwise, false
        """
        RequiresEmailCredits = None #bool

        """
        Amount of credits added to Account automatically
        """
        MonthlyRefillCredits = None #double

        """
        True, if Account can request for private IP on its own. Otherwise, false
        """
        EnablePrivateIPRequest = None #bool

        """
        Amount of emails sent from this Account
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
        Amount of emails Account can send daily
        """
        DailySendLimit = None #long

        """
        Account's current status.
        """
        Status = None #string

        """
        Maximum size of email including attachments in MB's
        """
        EmailSizeLimit = None #int

        """
        Maximum number of contacts the Account can have
        """
        MaxContacts = None #int

        """
        Sending permission setting for Account
        """
        SendingPermission = None #ApiTypes.SendingPermission

        """
        
        """
        HasModify2FA = None #bool

        """
        
        """
        ContactsCount = None #int


    """
    Detailed settings of Sub-Account.
    """
    class SubAccountSettings:
        """
        Proper email address.
        """
        Email = None #string

        """
        True, if Account needs credits to send emails. Otherwise, false
        """
        RequiresEmailCredits = None #bool

        """
        Amount of credits added to Account automatically
        """
        MonthlyRefillCredits = None #double

        """
        Maximum size of email including attachments in MB's
        """
        EmailSizeLimit = None #int

        """
        Amount of emails Account can send daily
        """
        DailySendLimit = None #int

        """
        Maximum number of contacts the Account can have
        """
        MaxContacts = None #int

        """
        True, if Account can request for private IP on its own. Otherwise, false
        """
        EnablePrivateIPRequest = None #bool

        """
        True, if you want to use Contact Delivery Tools.  Otherwise, false
        """
        EnableContactFeatures = None #bool

        """
        Sending permission setting for Account
        """
        SendingPermission = None #ApiTypes.SendingPermission

        """
        Name of your custom IP Pool to be used in the sending process
        """
        PoolName = None #string

        """
        
        """
        PublicAccountID = None #string

        """
        True, if you want to allow two-factor authentication.  Otherwise, false.
        """
        Allow2FA = None #bool?


    """
    
    """
    class SubaccountSummary:
        """
        
        """
        EmailsSentToday = None #int

        """
        
        """
        EmailsSentThisMonth = None #int


    """
    Add-on support options for your Account.
    """
    class SupportPlan(Enum):
        """
        In-app support option for $1/day.
        """
        Priority = 1

        """
        In-app real-time chat support option for $7/day.
        """
        Premium = 2


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
        AMP code of email (needs escaping).
        """
        BodyAmp = None #string

        """
        Text body of email.
        """
        BodyText = None #string

        """
        ID number of original template.
        """
        OriginalTemplateID = None #int

        """
        
        """
        OriginalTemplateName = None #string

        """
        Enum: 0 - private, 1 - public, 2 - mockup
        """
        TemplateScope = None #ApiTypes.TemplateScope

        """
        Template's Tags
        """
        Tags = None #List<string>


    """
    List of templates (including drafts)
    """
    class TemplateList:
        """
        List of templates
        """
        Templates = None #List<ApiTypes.Template>

        """
        Total of templates
        """
        TemplatesCount = None #int

        """
        List of draft templates
        """
        DraftTemplate = None #List<ApiTypes.Template>

        """
        Total of draft templates
        """
        DraftTemplatesCount = None #int


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
        Template is a temporary draft, not to be used permanently.
        """
        Draft = 2


    """
    Tag used for tagging multiple Templates
    """
    class TemplateTag:
        """
        Tag's value
        """
        Name = None #string


    """
    A list of your personal and global Template Tags
    """
    class TemplateTagList:
        """
        List of personal Tags
        """
        Tags = None #List<ApiTypes.TemplateTag>

        """
        List of globally available Tags
        """
        GlobalTags = None #List<ApiTypes.TemplateTag>


    """
    
    """
    class TemplateType(Enum):
        """
        Template supports any valid HTML
        """
        RawHTML = 0

        """
        Template is created for email and can only be modified in the drag and drop email editor
        """
        DragDropEditor = 1

        """
        Template is created for landing page and can only be modified in the drag and drop langing page editor
        """
        LandingPageEditor = 2


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
    HTTP or HTTPS Protocal used for link tracking.
    """
    class TrackingType(Enum):
        """
        Tracking protocal that is not encrypted.
        """
        Http = 0

        """
        Tracking protocal using an external SSL Certificate for encryption.
        """
        ExternalHttps = 1

        """
        Tracking protocal using an internal SSL Certificate for encyrption.
        """
        InternalCertHttps = 2

        """
        Tracking protocal using LetsEncrypt Certificate for encryption.
        """
        LetsEncryptCert = 3


    """
    Status of ValidDomain to determine how often tracking validation should be performed.
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
        True, if this Account is a Sub-Account. Otherwise, false
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
        Cost of email credits
        """
        EmailCreditsCost = None #int?

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
        
        """
        VerificationCost = None #decimal

        """
        
        """
        VerificationCount = None #int

        """
        
        """
        InboundEmailCost = None #decimal

        """
        
        """
        InboundEmailCount = None #int


    """
    
    """
    class ValidationError:
        """
        
        """
        TXTRecord = None #string

        """
        
        """
        Error = None #string


    """
    
    """
    class ValidationStatus:
        """
        
        """
        IsValid = None #bool

        """
        
        """
        Errors = None #List<ApiTypes.ValidationError>

        """
        
        """
        Log = None #string


    """
    
    """
    class ValidEmail:
        """
        
        """
        ValidEmailID = None #int

        """
        Proper email address.
        """
        Email = None #string

        """
        
        """
        Validated = None #bool


    """
    Notification webhook setting
    """
    class Webhook:
        """
        Public webhook ID
        """
        WebhookID = None #string

        """
        Filename
        """
        Name = None #string

        """
        Creation date.
        """
        DateCreated = None #DateTime?

        """
        Last change date
        """
        DateUpdated = None #DateTime?

        """
        URL of notification.
        """
        URL = None #string

        """
        
        """
        NotifyOncePerEmail = None #bool

        """
        
        """
        NotificationForSent = None #bool

        """
        
        """
        NotificationForOpened = None #bool

        """
        
        """
        NotificationForClicked = None #bool

        """
        
        """
        NotificationForUnsubscribed = None #bool

        """
        
        """
        NotificationForAbuseReport = None #bool

        """
        
        """
        NotificationForError = None #bool


    """
    Lists web notification options of your account.
    """
    class WebNotificationOptions:
        """
        URL address to receive web notifications to parse and process.
        """
        WebNotificationUrl = None #string

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
Manage your AccessTokens (ApiKeys)
"""
class AccessToken:

    def Add(tokenName, accessLevel):
        """
        Add new AccessToken with appropriate AccessLevel (permission).
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string tokenName - Name of the AccessToken for ease of reference.
            ApiTypes.AccessLevel accessLevel - Level of access (permission) to our API.
        Returns string
        """
        parameters = { 
                    'tokenName': tokenName,
                    'accessLevel': accessLevel.value}

        return ApiClient.Request('GET', '/accesstoken/add', parameters)

    def Delete(tokenName):
        """
        Permanently delete AccessToken from your Account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string tokenName - Name of the AccessToken for ease of reference.
        """
        parameters = { 
                    'tokenName': tokenName}

        return ApiClient.Request('GET', '/accesstoken/delete', parameters)

    def List():
        """
        List all the AccessToken's in your Account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.AccessToken>
        """

        return ApiClient.Request('GET', '/accesstoken/list', parameters)

    def Update(tokenName, accessLevel, newTokenName = None):
        """
        Update AccessToken with a new name or AccessLevel.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string tokenName - Name of the AccessToken for ease of reference.
            ApiTypes.AccessLevel accessLevel - Level of access (permission) to our API.
            string newTokenName - New name of the AccessToken. (default None)
        """
        parameters = { 
                    'tokenName': tokenName,
                    'accessLevel': accessLevel.value,
                    'newTokenName': newTokenName}

        return ApiClient.Request('GET', '/accesstoken/update', parameters)


""" 
Methods for managing your account and subaccounts.
"""
class Account:

    def AddDedicatedSupport(supportPlan):
        """
        Request premium support for your account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            ApiTypes.SupportPlan supportPlan - 
        """
        parameters = { 
                    'supportPlan': supportPlan.value}

        return ApiClient.Request('GET', '/account/adddedicatedsupport', parameters)

    def AddSubAccount(email, password, confirmPassword, allow2fa = False, requiresEmailCredits = False, maxContacts = 0, enablePrivateIPRequest = True, sendActivation = False, returnUrl = None, sendingPermission = None, enableContactFeatures = None, poolName = None, emailSizeLimit = 10, dailySendLimit = None):
        """
        Create new subaccount and provide most important data about it.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string email - Proper email address.
            string password - Current password.
            string confirmPassword - Repeat new password.
            bool allow2fa - True, if you want to allow two-factor authentication.  Otherwise, false. (default False)
            bool requiresEmailCredits - True, if Account needs credits to send emails. Otherwise, false (default False)
            int maxContacts - Maximum number of contacts the Account can have (default 0)
            bool enablePrivateIPRequest - True, if Account can request for private IP on its own. Otherwise, false (default True)
            bool sendActivation - True, if you want to send activation email to this Account. Otherwise, false (default False)
            string returnUrl - URL to navigate to after Account creation (default None)
            ApiTypes.SendingPermission? sendingPermission - Sending permission setting for Account (default None)
            bool? enableContactFeatures - Private IP required. Name of the custom IP Pool which Sub Account should use to send its emails. Leave empty for the default one or if no Private IPs have been bought (default None)
            string poolName - Name of your custom IP Pool to be used in the sending process (default None)
            int emailSizeLimit - Maximum size of email including attachments in MB's (default 10)
            int? dailySendLimit - Amount of emails Account can send daily (default None)
        Returns string
        """
        parameters = { 
                    'email': email,
                    'password': password,
                    'confirmPassword': confirmPassword,
                    'allow2fa': allow2fa,
                    'requiresEmailCredits': requiresEmailCredits,
                    'maxContacts': maxContacts,
                    'enablePrivateIPRequest': enablePrivateIPRequest,
                    'sendActivation': sendActivation,
                    'returnUrl': returnUrl,
                    'sendingPermission': sendingPermission.value,
                    'enableContactFeatures': enableContactFeatures,
                    'poolName': poolName,
                    'emailSizeLimit': emailSizeLimit,
                    'dailySendLimit': dailySendLimit}

        return ApiClient.Request('GET', '/account/addsubaccount', parameters)

    def AddSubAccountCredits(credits, notes, subAccountEmail = None, publicAccountID = None):
        """
        Add email credits to a sub-account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int credits - Amount of credits to add
            string notes - Specific notes about the transaction
            string subAccountEmail - Email address of Sub-Account (default None)
            string publicAccountID - Public key of sub-account to add credits to. Use subAccountEmail or publicAccountID not both. (default None)
        """
        parameters = { 
                    'credits': credits,
                    'notes': notes,
                    'subAccountEmail': subAccountEmail,
                    'publicAccountID': publicAccountID}

        return ApiClient.Request('GET', '/account/addsubaccountcredits', parameters)

    def AddWebhook(webNotificationUrl, name, notifyOncePerEmail = None, notificationForSent = None, notificationForOpened = None, notificationForClicked = None, notificationForUnsubscribed = None, notificationForAbuseReport = None, notificationForError = None):
        """
        Add notifications webhook
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string webNotificationUrl - URL address to receive web notifications to parse and process.
            string name - Filename
            bool? notifyOncePerEmail -  (default None)
            bool? notificationForSent -  (default None)
            bool? notificationForOpened -  (default None)
            bool? notificationForClicked -  (default None)
            bool? notificationForUnsubscribed -  (default None)
            bool? notificationForAbuseReport -  (default None)
            bool? notificationForError -  (default None)
        Returns string
        """
        parameters = { 
                    'webNotificationUrl': webNotificationUrl,
                    'name': name,
                    'notifyOncePerEmail': notifyOncePerEmail,
                    'notificationForSent': notificationForSent,
                    'notificationForOpened': notificationForOpened,
                    'notificationForClicked': notificationForClicked,
                    'notificationForUnsubscribed': notificationForUnsubscribed,
                    'notificationForAbuseReport': notificationForAbuseReport,
                    'notificationForError': notificationForError}

        return ApiClient.Request('GET', '/account/addwebhook', parameters)

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

    def ChangePassword(newPassword, confirmPassword, resetApiKey = False, currentPassword = None):
        """
        Create new password for your account. Password needs to be at least 6 characters long.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string newPassword - New password for Account.
            string confirmPassword - Repeat new password.
            bool resetApiKey -  (default False)
            string currentPassword - Current password. (default None)
        """
        parameters = { 
                    'newPassword': newPassword,
                    'confirmPassword': confirmPassword,
                    'resetApiKey': resetApiKey,
                    'currentPassword': currentPassword}

        return ApiClient.Request('GET', '/account/changepassword', parameters)

    def ChangeSubAccountPassword(newPassword, confirmPassword, subAccountEmail, resetApiKey = False):
        """
        Create new password for subaccount. Password needs to be at least 6 characters long.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string newPassword - New password for Account.
            string confirmPassword - Repeat new password.
            string subAccountEmail - Email address of Sub-Account
            bool resetApiKey -  (default False)
        """
        parameters = { 
                    'newPassword': newPassword,
                    'confirmPassword': confirmPassword,
                    'subAccountEmail': subAccountEmail,
                    'resetApiKey': resetApiKey}

        return ApiClient.Request('GET', '/account/changesubaccountpassword', parameters)

    def DeleteSubAccount(subAccountEmail = None, publicAccountID = None):
        """
        Deletes specified Subaccount
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string subAccountEmail - Email address of Sub-Account (default None)
            string publicAccountID - Public key of sub-account to delete. Use subAccountEmail or publicAccountID not both. (default None)
        """
        parameters = { 
                    'subAccountEmail': subAccountEmail,
                    'publicAccountID': publicAccountID}

        return ApiClient.Request('GET', '/account/deletesubaccount', parameters)

    def DeleteWebhook(webhookID):
        """
        Delete notifications webhook
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string webhookID - 
        """
        parameters = { 
                    'webhookID': webhookID}

        return ApiClient.Request('GET', '/account/deletewebhook', parameters)

    def GetSubAccountApiKey(subAccountEmail = None, publicAccountID = None):
        """
        Returns API Key for the given Sub Account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string subAccountEmail - Email address of Sub-Account (default None)
            string publicAccountID - Public key of sub-account to retrieve sub-account API Key. Use subAccountEmail or publicAccountID not both. (default None)
        Returns string
        """
        parameters = { 
                    'subAccountEmail': subAccountEmail,
                    'publicAccountID': publicAccountID}

        return ApiClient.Request('GET', '/account/getsubaccountapikey', parameters)

    def GetSubAccountList(limit = 0, offset = 0, email = None):
        """
        Lists all of your subaccounts
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int limit - Maximum number of returned items. (default 0)
            int offset - How many items should be returned ahead. (default 0)
            string email - Proper email address. (default None)
        Returns List<ApiTypes.SubAccount>
        """
        parameters = { 
                    'limit': limit,
                    'offset': offset,
                    'email': email}

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

    def LoadInboundOptions():
        """
        Load inbound options of your account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns ApiTypes.InboundOptions
        """

        return ApiClient.Request('GET', '/account/loadinboundoptions', parameters)

    def LoadPaymentHistory(limit, offset, fromDate, toDate):
        """
        Lists all payments
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int limit - Maximum number of returned items.
            int offset - How many items should be returned ahead.
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

    def LoadReputationHistory():
        """
        Shows latest changes in your sending reputation
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.ReputationHistory>
        """

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
            int limit - Maximum number of returned items. (default 20)
            int offset - How many items should be returned ahead. (default 0)
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
            string subAccountEmail - Email address of Sub-Account (default None)
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
            string subAccountEmail - Email address of Sub-Account (default None)
            string publicAccountID - Public key of sub-account to load settings for. Use subAccountEmail or publicAccountID not both. (default None)
        Returns ApiTypes.SubAccountSettings
        """
        parameters = { 
                    'subAccountEmail': subAccountEmail,
                    'publicAccountID': publicAccountID}

        return ApiClient.Request('GET', '/account/loadsubaccountsettings', parameters)

    def LoadUsage(EEfrom, to, loadSubaccountsUsage = True):
        """
        Shows usage of your account in given time.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            DateTime from - Starting date for search in YYYY-MM-DDThh:mm:ss format.
            DateTime to - Ending date for search in YYYY-MM-DDThh:mm:ss format.
            bool loadSubaccountsUsage -  (default True)
        Returns List<ApiTypes.Usage>
        """
        parameters = { 
                    'from': EEfrom,
                    'to': to,
                    'loadSubaccountsUsage': loadSubaccountsUsage}

        return ApiClient.Request('GET', '/account/loadusage', parameters)

    def LoadWebhook(limit = 0, offset = 0):
        """
        Load notifications webhooks
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int limit - Maximum number of returned items. (default 0)
            int offset - How many items should be returned ahead. (default 0)
        Returns List<ApiTypes.Webhook>
        """
        parameters = { 
                    'limit': limit,
                    'offset': offset}

        return ApiClient.Request('GET', '/account/loadwebhook', parameters)

    def LoadWebNotificationOptions():
        """
        Load web notification options of your account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns ApiTypes.WebNotificationOptions
        """

        return ApiClient.Request('GET', '/account/loadwebnotificationoptions', parameters)

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

    def RemoveSubAccountCredits(notes, subAccountEmail = None, publicAccountID = None, credits = None, removeAll = False):
        """
        Remove email credits from a sub-account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string notes - Specific notes about the transaction
            string subAccountEmail - Email address of Sub-Account (default None)
            string publicAccountID - Public key of sub-account to remove credits from. Use subAccountEmail or publicAccountID not both. (default None)
            int? credits - Amount of credits to remove (default None)
            bool removeAll - Remove all credits of this type from sub-account (overrides credits if provided) (default False)
        """
        parameters = { 
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

    def UpdateAdvancedOptions(enableClickTracking = None, enableLinkClickTracking = None, manageSubscriptions = None, manageSubscribedOnly = None, transactionalOnUnsubscribe = None, skipListUnsubscribe = None, autoTextFromHtml = None, allowCustomHeaders = None, bccEmail = None, contentTransferEncoding = None, emailNotificationForError = None, emailNotificationEmail = None, lowCreditNotification = None, enableUITooltips = None, notificationsEmails = None, unsubscribeNotificationsEmails = None, logoUrl = None, enableTemplateScripting = True, staleContactScore = None, staleContactInactiveDays = None, deliveryReason = None, tutorialsEnabled = None, enableOpenTracking = None, consentTrackingOnUnsubscribe = None):
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
            bool? lowCreditNotification - True, if you want to receive low credit email notifications. Otherwise, false (default None)
            bool? enableUITooltips - True, if Account has tooltips active. Otherwise, false (default None)
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
                    'lowCreditNotification': lowCreditNotification,
                    'enableUITooltips': enableUITooltips,
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

    def UpdateCustomBranding(enablePrivateBranding = False, logoUrl = None, supportLink = None, privateBrandingUrl = None, smtpAddress = None, smtpAlternative = None, paymentUrl = None, customBouncesDomain = None):
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
            string customBouncesDomain -  (default None)
        """
        parameters = { 
                    'enablePrivateBranding': enablePrivateBranding,
                    'logoUrl': logoUrl,
                    'supportLink': supportLink,
                    'privateBrandingUrl': privateBrandingUrl,
                    'smtpAddress': smtpAddress,
                    'smtpAlternative': smtpAlternative,
                    'paymentUrl': paymentUrl,
                    'customBouncesDomain': customBouncesDomain}

        return ApiClient.Request('GET', '/account/updatecustombranding', parameters)

    def UpdateInboundNotifications(inboundContactsOnly = None, hubCallBackUrl = "", inboundDomain = None):
        """
        Update inbound notifications options of your account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            bool? inboundContactsOnly - True, if you want inbound email to only process contacts from your Account. Otherwise, false (default None)
            string hubCallBackUrl - URL used for tracking action of inbound emails (default "")
            string inboundDomain - Domain you use as your inbound domain (default None)
        Returns ApiTypes.InboundOptions
        """
        parameters = { 
                    'inboundContactsOnly': inboundContactsOnly,
                    'hubCallBackUrl': hubCallBackUrl,
                    'inboundDomain': inboundDomain}

        return ApiClient.Request('GET', '/account/updateinboundnotifications', parameters)

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

    def UpdateSubAccountSettings(requiresEmailCredits = False, allow2fa = None, monthlyRefillCredits = 0, dailySendLimit = None, emailSizeLimit = 10, enablePrivateIPRequest = False, maxContacts = 0, subAccountEmail = None, publicAccountID = None, sendingPermission = None, enableContactFeatures = None, poolName = None):
        """
        Updates settings of specified subaccount
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            bool requiresEmailCredits - True, if Account needs credits to send emails. Otherwise, false (default False)
            bool? allow2fa - True, if you want to allow two-factor authentication.  Otherwise, false. (default None)
            int monthlyRefillCredits - Amount of credits added to Account automatically (default 0)
            int? dailySendLimit - Amount of emails Account can send daily (default None)
            int emailSizeLimit - Maximum size of email including attachments in MB's (default 10)
            bool enablePrivateIPRequest - True, if Account can request for private IP on its own. Otherwise, false (default False)
            int maxContacts - Maximum number of contacts the Account can have (default 0)
            string subAccountEmail - Email address of Sub-Account (default None)
            string publicAccountID - Public key of sub-account to update. Use subAccountEmail or publicAccountID not both. (default None)
            ApiTypes.SendingPermission? sendingPermission - Sending permission setting for Account (default None)
            bool? enableContactFeatures - True, if you want to use Contact Delivery Tools.  Otherwise, false (default None)
            string poolName - Name of your custom IP Pool to be used in the sending process (default None)
        """
        parameters = { 
                    'requiresEmailCredits': requiresEmailCredits,
                    'allow2fa': allow2fa,
                    'monthlyRefillCredits': monthlyRefillCredits,
                    'dailySendLimit': dailySendLimit,
                    'emailSizeLimit': emailSizeLimit,
                    'enablePrivateIPRequest': enablePrivateIPRequest,
                    'maxContacts': maxContacts,
                    'subAccountEmail': subAccountEmail,
                    'publicAccountID': publicAccountID,
                    'sendingPermission': sendingPermission.value,
                    'enableContactFeatures': enableContactFeatures,
                    'poolName': poolName}

        return ApiClient.Request('GET', '/account/updatesubaccountsettings', parameters)

    def UpdateWebhook(webhookID, name = None, webNotificationUrl = None, notifyOncePerEmail = None, notificationForSent = None, notificationForOpened = None, notificationForClicked = None, notificationForUnsubscribed = None, notificationForAbuseReport = None, notificationForError = None):
        """
        Update notification webhook
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string webhookID - 
            string name - Filename (default None)
            string webNotificationUrl - URL address to receive web notifications to parse and process. (default None)
            bool? notifyOncePerEmail -  (default None)
            bool? notificationForSent -  (default None)
            bool? notificationForOpened -  (default None)
            bool? notificationForClicked -  (default None)
            bool? notificationForUnsubscribed -  (default None)
            bool? notificationForAbuseReport -  (default None)
            bool? notificationForError -  (default None)
        """
        parameters = { 
                    'webhookID': webhookID,
                    'name': name,
                    'webNotificationUrl': webNotificationUrl,
                    'notifyOncePerEmail': notifyOncePerEmail,
                    'notificationForSent': notificationForSent,
                    'notificationForOpened': notificationForOpened,
                    'notificationForClicked': notificationForClicked,
                    'notificationForUnsubscribed': notificationForUnsubscribed,
                    'notificationForAbuseReport': notificationForAbuseReport,
                    'notificationForError': notificationForError}

        return ApiClient.Request('GET', '/account/updatewebhook', parameters)


""" 
Manage all aspects of your Campaigns.
"""
class Campaign:

    def Add(campaign):
        """
        Adds a Campaign to the queue for processing based on the configuration.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            ApiTypes.Campaign campaign - JSON representation of a campaign
        Returns int
        """
        parameters = { 
                    'campaign': campaign}

        return ApiClient.Request('GET', '/campaign/add', parameters)

    def Copy(channelID, newCampaignName = None):
        """
        Makes a copy of a campaign configuration and leaves it in draft mode for further editing.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int channelID - ID number of selected Channel.
            string newCampaignName -  (default None)
        Returns int
        """
        parameters = { 
                    'channelID': channelID,
                    'newCampaignName': newCampaignName}

        return ApiClient.Request('GET', '/campaign/copy', parameters)

    def Delete(channelID):
        """
        Deletes the Campaign.  This will not cancel emails that are in progress, see /log/cancelinprogress for this option.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int channelID - ID number of selected Channel.
        """
        parameters = { 
                    'channelID': channelID}

        return ApiClient.Request('GET', '/campaign/delete', parameters)

    def Export(channelIDs = {}, fileFormat = ApiTypes.ExportFileFormats.Csv, compressionFormat = ApiTypes.CompressionFormat.EENone, fileName = None):
        """
        Export Campaign data to the chosen file format.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<int> channelIDs - List of campaign IDs used for processing (default None)
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file including extension. (default None)
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
        Returns a list all of your Campaigns.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string search - Text fragment used for searching. (default None)
            int offset - How many items should be returned ahead. (default 0)
            int limit - Maximum number of returned items. (default 0)
        Returns List<ApiTypes.CampaignChannel>
        """
        parameters = { 
                    'search': search,
                    'offset': offset,
                    'limit': limit}

        return ApiClient.Request('GET', '/campaign/list', parameters)

    def Update(campaign):
        """
        Updates a previously added Campaign.  Only Active and Paused campaigns can be updated.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            ApiTypes.Campaign campaign - JSON representation of a campaign
        Returns int
        """
        parameters = { 
                    'campaign': campaign}

        return ApiClient.Request('GET', '/campaign/update', parameters)


""" 
Manage SMTP and HTTP API Channels for grouping email delivery.
"""
class Channel:

    def Add(name):
        """
        Manually add a Channel to your Account to group email.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string name - Descriptive name of the channel.
        Returns string
        """
        parameters = { 
                    'name': name}

        return ApiClient.Request('GET', '/channel/add', parameters)

    def Delete(name):
        """
        Delete the selected Channel.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string name - The name of the Channel to delete.
        """
        parameters = { 
                    'name': name}

        return ApiClient.Request('GET', '/channel/delete', parameters)

    def Export(channelNames, fileFormat = ApiTypes.ExportFileFormats.Csv, compressionFormat = ApiTypes.CompressionFormat.EENone, fileName = None):
        """
        Export selected Channels to chosen file format.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<string> channelNames - List of channel names used for processing
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file including extension. (default None)
        Returns ApiTypes.ExportLink
        """
        parameters = { 
                    'channelNames': ";".join(map(str, channelNames)),
                    'fileFormat': fileFormat.value,
                    'compressionFormat': compressionFormat.value,
                    'fileName': fileName}

        return ApiClient.Request('GET', '/channel/export', parameters)

    def List(limit = 0, offset = 0):
        """
        Returns a list your Channels.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int limit - Maximum number of returned items. (default 0)
            int offset - How many items should be returned ahead. (default 0)
        Returns List<ApiTypes.Channel>
        """
        parameters = { 
                    'limit': limit,
                    'offset': offset}

        return ApiClient.Request('GET', '/channel/list', parameters)

    def Update(name, newName):
        """
        Rename an existing Channel.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string name - The name of the Channel to update.
            string newName - The new name for the Channel.
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

    def Add(publicAccountID, email, publicListID = {}, listName = {}, firstName = None, lastName = None, source = ApiTypes.ContactSource.ContactApi, returnUrl = None, sourceUrl = None, activationReturnUrl = None, activationTemplate = None, sendActivation = True, consentDate = None, consentIP = None, field = {}, notifyEmail = None, alreadyActiveUrl = None, consentTracking = ApiTypes.ConsentTracking.Unknown):
        """
        Add a new contact and optionally to one of your lists.  Note that your API KEY is not required for this call.
            string publicAccountID - 
            string email - Proper email address.
            IEnumerable<string> publicListID - ID code of list (default None)
            IEnumerable<string> listName - Name of your list. (default None)
            string firstName - First name. (default None)
            string lastName - Last name. (default None)
            ApiTypes.ContactSource source - Specifies the way of uploading the contact (default ApiTypes.ContactSource.ContactApi)
            string returnUrl - URL to navigate to after Account creation (default None)
            string sourceUrl - URL from which request was sent. (default None)
            string activationReturnUrl - The url to return the contact to after activation. (default None)
            string activationTemplate - Custom template to use for sending double opt-in activation emails. (default None)
            bool sendActivation - True, if you want to send activation email to this contact. Otherwise, false (default True)
            DateTime? consentDate - Date of consent to send this contact(s) your email. If not provided current date is used for consent. (default None)
            string consentIP - IP address of consent to send this contact(s) your email. If not provided your current public IP address is used for consent. (default None)
            Dictionary<string, string> field - Custom contact field like companyname, customernumber, city etc. Request parameters prefixed by field_ like field_companyname, field_customernumber, field_city (default None)
            string notifyEmail - Emails, separated by semicolon, to which the notification about contact subscribing should be sent to (default None)
            string alreadyActiveUrl - Url to navigate to if contact already is subscribed (default None)
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
            ApiTypes.ContactStatus status - Status of the given resource
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
            ApiTypes.ContactStatus status - Status of the given resource
            string rule - Query used for filtering. (default None)
            IEnumerable<string> emails - Comma delimited list of contact emails (default None)
        """
        parameters = { 
                    'status': status.value,
                    'rule': rule,
                    'emails': ";".join(map(str, emails))}

        return ApiClient.Request('GET', '/contact/changestatus', parameters)

    def CountByStatus(rule = None):
        """
        Returns number of Contacts, RULE specifies contact Status.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string rule - Query used for filtering. (default None)
        Returns ApiTypes.ContactStatusCounts
        """
        parameters = { 
                    'rule': rule}

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
        Permanently deletes the contacts provided.  You can provide either a qualified rule or a list of emails (comma separated string).
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
            string fileName - Name of your file including extension. (default None)
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
            string fileName - Name of your file including extension. (default None)
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
            int limit - Maximum number of returned items. (default 20)
            int offset - How many items should be returned ahead. (default 0)
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
            int limit - Maximum number of returned items. (default 20)
            int offset - How many items should be returned ahead. (default 0)
        Returns List<ApiTypes.Contact>
        """
        parameters = { 
                    'segmentName': segmentName,
                    'limit': limit,
                    'offset': offset}

        return ApiClient.Request('GET', '/contact/getcontactsbysegment', parameters)

    def List(rule = None, limit = 20, offset = 0, sort = None):
        """
        List of all contacts. If you have not specified RULE, all Contacts will be listed.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string rule - Query used for filtering. (default None)
            int limit - Maximum number of returned items. (default 20)
            int offset - How many items should be returned ahead. (default 0)
            ApiTypes.ContactSort? sort -  (default None)
        Returns List<ApiTypes.Contact>
        """
        parameters = { 
                    'rule': rule,
                    'limit': limit,
                    'offset': offset,
                    'sort': sort.value}

        return ApiClient.Request('GET', '/contact/list', parameters)

    def LoadBlocked(statuses, search = None, limit = 0, offset = 0):
        """
        Load blocked contacts
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<ApiTypes.ContactStatus> statuses - List of blocked statuses: Abuse, Bounced or Unsubscribed
            string search - Text fragment used for searching. (default None)
            int limit - Maximum number of returned items. (default 0)
            int offset - How many items should be returned ahead. (default 0)
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
            int limit - Maximum number of returned items. (default 0)
            int offset - How many items should be returned ahead. (default 0)
        Returns List<ApiTypes.ContactHistory>
        """
        parameters = { 
                    'email': email,
                    'limit': limit,
                    'offset': offset}

        return ApiClient.Request('GET', '/contact/loadhistory', parameters)

    def QuickAdd(emails, firstName = None, lastName = None, publicListID = None, listName = None, status = ApiTypes.ContactStatus.Active, notes = None, consentDate = None, consentIP = None, field = {}, notifyEmail = None, consentTracking = ApiTypes.ConsentTracking.Unknown, source = ApiTypes.ContactSource.ManualInput):
        """
        Add new Contact to one of your Lists.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<string> emails - Comma delimited list of contact emails
            string firstName - First name. (default None)
            string lastName - Last name. (default None)
            string publicListID - ID code of list (default None)
            string listName - Name of your list. (default None)
            ApiTypes.ContactStatus status - Status of the given resource (default ApiTypes.ContactStatus.Active)
            string notes - Free form field of notes (default None)
            DateTime? consentDate - Date of consent to send this contact(s) your email. If not provided current date is used for consent. (default None)
            string consentIP - IP address of consent to send this contact(s) your email. If not provided your current public IP address is used for consent. (default None)
            Dictionary<string, string> field - Custom contact field like companyname, customernumber, city etc. Request parameters prefixed by field_ like field_companyname, field_customernumber, field_city (default None)
            string notifyEmail - Emails, separated by semicolon, to which the notification about contact subscribing should be sent to (default None)
            ApiTypes.ConsentTracking consentTracking -  (default ApiTypes.ConsentTracking.Unknown)
            ApiTypes.ContactSource source - Specifies the way of uploading the contact (default ApiTypes.ContactSource.ManualInput)
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
                    'consentTracking': consentTracking.value,
                    'source': source.value}
        ApiClient.AddDictionaryParameter(field, "field", parameters)

        return ApiClient.Request('GET', '/contact/quickadd', parameters)

    def Subscribe(publicAccountID):
        """
        Basic double opt-in email subscribe form for your account.  This can be used for contacts that need to re-subscribe as well.
            string publicAccountID - 
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
            Dictionary<string, string> field - Custom contact field like companyname, customernumber, city etc. Request parameters prefixed by field_ like field_companyname, field_customernumber, field_city (default None)
            string customFields - Custom contact field like companyname, customernumber, city etc. JSON serialized text like { "city":"london" }  (default None)
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
            ApiTypes.ContactStatus status - Status of the given resource (default ApiTypes.ContactStatus.Active)
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
Manage sending domains and verify DNS configurations.
"""
class Domain:

    def Add(domain, trackingType = ApiTypes.TrackingType.Http, setAsDefault = False):
        """
        Add a new domain to be registered and secured to an Account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Name of selected domain.
            ApiTypes.TrackingType trackingType -  (default ApiTypes.TrackingType.Http)
            bool setAsDefault - Set this domain as the default domain for the Account. (default False)
        """
        parameters = { 
                    'domain': domain,
                    'trackingType': trackingType.value,
                    'setAsDefault': setAsDefault}

        return ApiClient.Request('GET', '/domain/add', parameters)

    def Delete(domain):
        """
        Deletes a domain from the Account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Name of selected domain.
        """
        parameters = { 
                    'domain': domain}

        return ApiClient.Request('GET', '/domain/delete', parameters)

    def List():
        """
        Lists all the domains configured for this Account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.DomainDetail>
        """

        return ApiClient.Request('GET', '/domain/list', parameters)

    def SetDefault(email):
        """
        Sets the default sender for the Account as an email address from a verified domain.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string email - Email address of a verified domain to be used as default when sending from non-verified domains.
        """
        parameters = { 
                    'email': email}

        return ApiClient.Request('GET', '/domain/setdefault', parameters)

    def SetVerp(domain, isVerp, customBouncesDomain = None, isCustomBouncesDomainDefault = False):
        """
        Allow to use VERP on given domain and specify custom bounces domain.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Name of selected domain.
            bool isVerp - 
            string customBouncesDomain -  (default None)
            bool isCustomBouncesDomainDefault -  (default False)
        """
        parameters = { 
                    'domain': domain,
                    'isVerp': isVerp,
                    'customBouncesDomain': customBouncesDomain,
                    'isCustomBouncesDomainDefault': isCustomBouncesDomainDefault}

        return ApiClient.Request('GET', '/domain/setverp', parameters)

    def VerifyDkim(domain):
        """
        Verifies proper DKIM DNS configuration for the domain.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Domain name to verify.
        Returns string
        """
        parameters = { 
                    'domain': domain}

        return ApiClient.Request('GET', '/domain/verifydkim', parameters)

    def VerifyMX(domain):
        """
        Verifies proper MX DNS configuration for the domain.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Domain name to verify.
        Returns string
        """
        parameters = { 
                    'domain': domain}

        return ApiClient.Request('GET', '/domain/verifymx', parameters)

    def VerifySpf(domain):
        """
        Verifies proper SPF DNS configuration for the domain.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Domain name to verifiy.
        Returns ApiTypes.ValidationStatus
        """
        parameters = { 
                    'domain': domain}

        return ApiClient.Request('GET', '/domain/verifyspf', parameters)

    def VerifyTracking(domain, trackingType = ApiTypes.TrackingType.Http):
        """
        Verifies proper CNAME DNS configuration for the tracking domain.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string domain - Domain name to verify.
            ApiTypes.TrackingType trackingType -  (default ApiTypes.TrackingType.Http)
        Returns string
        """
        parameters = { 
                    'domain': domain,
                    'trackingType': trackingType.value}

        return ApiClient.Request('GET', '/domain/verifytracking', parameters)


""" 
Send your emails and see their statuses
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

    def ListAttachments(msgID):
        """
        Lists the file attachments for the specified email.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string msgID - ID number of selected message.
        Returns List<ApiTypes.File>
        """
        parameters = { 
                    'msgID': msgID}

        return ApiClient.Request('GET', '/email/listattachments', parameters)

    def Send(subject = None, EEfrom = None, fromName = None, sender = None, senderName = None, msgFrom = None, msgFromName = None, replyTo = None, replyToName = None, to = {}, msgTo = {}, msgCC = {}, msgBcc = {}, lists = {}, segments = {}, mergeSourceFilename = None, dataSource = None, channel = None, bodyHtml = None, bodyText = None, charset = None, charsetBodyHtml = None, charsetBodyText = None, encodingType = ApiTypes.EncodingType.EENone, template = None, attachmentFiles = {}, headers = {}, postBack = None, merge = {}, timeOffSetMinutes = None, poolName = None, isTransactional = False, attachments = {}, trackOpens = None, trackClicks = None, utmSource = None, utmMedium = None, utmCampaign = None, utmContent = None, bodyAmp = None, charsetBodyAmp = None):
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
            string dataSource - Name or ID of the previously uploaded file (via the File/Upload request) which should be a CSV list of Recipients. (default None)
            string channel - An ID field (max 191 chars) that can be used for reporting [will default to HTTP API or SMTP API] (default None)
            string bodyHtml - Html email body (default None)
            string bodyText - Text email body (default None)
            string charset - Text value of charset encoding for example: iso-8859-1, windows-1251, utf-8, us-ascii, windows-1250 and more… (default None)
            string charsetBodyHtml - Sets charset for body html MIME part (overrides default value from charset parameter) (default None)
            string charsetBodyText - Sets charset for body text MIME part (overrides default value from charset parameter) (default None)
            ApiTypes.EncodingType encodingType - 0 for None, 1 for Raw7Bit, 2 for Raw8Bit, 3 for QuotedPrintable, 4 for Base64 (Default), 5 for Uue  note that you can also provide the text version such as "Raw7Bit" for value 1.  NOTE: Base64 or QuotedPrintable is recommended if you are validating your domain(s) with DKIM. (default ApiTypes.EncodingType.EENone)
            string template - The ID of an email template you have created in your account. (default None)
            IEnumerableFile attachmentFiles - Attachment files. These files should be provided with the POST multipart file upload and not directly in the request's URL. Can also include merge CSV file (default None)
            Dictionary<string, string> headers - Optional Custom Headers. Request parameters prefixed by headers_ like headers_customheader1, headers_customheader2. Note: a space is required after the colon before the custom header value. headers_xmailer=xmailer: header-value1 (default None)
            string postBack - Optional header returned in notifications. (default None)
            Dictionary<string, string> merge - Request parameters prefixed by merge_ like merge_firstname, merge_lastname. If sending to a template you can send merge_ fields to merge data with the template. Template fields are entered with {firstname}, {lastname} etc. (default None)
            string timeOffSetMinutes - Number of minutes in the future this email should be sent up to a maximum of 1 year (524160 minutes) (default None)
            string poolName - Name of your custom IP Pool to be used in the sending process (default None)
            bool isTransactional - True, if email is transactional (non-bulk, non-marketing, non-commercial). Otherwise, false (default False)
            IEnumerable<string> attachments - Names or IDs of attachments previously uploaded to your account (via the File/Upload request) that should be sent with this e-mail. (default None)
            bool? trackOpens - Should the opens be tracked? If no value has been provided, Account's default setting will be used. (default None)
            bool? trackClicks - Should the clicks be tracked? If no value has been provided, Account's default setting will be used. (default None)
            string utmSource - The utm_source marketing parameter appended to each link in the campaign. (default None)
            string utmMedium - The utm_medium marketing parameter appended to each link in the campaign. (default None)
            string utmCampaign - The utm_campaign marketing parameter appended to each link in the campaign. (default None)
            string utmContent - The utm_content marketing parameter appended to each link in the campaign. (default None)
            string bodyAmp - AMP email body (default None)
            string charsetBodyAmp - Sets charset for body AMP MIME part (overrides default value from charset parameter) (default None)
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
                    'trackClicks': trackClicks,
                    'utmSource': utmSource,
                    'utmMedium': utmMedium,
                    'utmCampaign': utmCampaign,
                    'utmContent': utmContent,
                    'bodyAmp': bodyAmp,
                    'charsetBodyAmp': charsetBodyAmp}
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

    def VerificationResult(txID):
        """
        Checks if verification emails is completed.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            Guid txID - 
        Returns ApiTypes.Export
        """
        parameters = { 
                    'txID': txID}

        return ApiClient.Request('GET', '/email/verificationresult', parameters)

    def Verify(email, uploadContact = False, updateStatus = False):
        """
        Verify single email address
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string email - Proper email address.
            bool uploadContact -  (default False)
            bool updateStatus - Should the existing contact's status be changed automatically based on the validation result (default False)
        Returns ApiTypes.EmailValidationResult
        """
        parameters = { 
                    'email': email,
                    'uploadContact': uploadContact,
                    'updateStatus': updateStatus}

        return ApiClient.Request('GET', '/email/verify', parameters)

    def VerifyList(emails = None, rule = None, listOfEmails = {}, uploadContacts = False, updateStatus = False):
        """
        Verify list of email addresses from file. Each email has to be in new line. This is asynchronous task. To check if task is completed use VerificationResult with returned task ID.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            File emails - Comma delimited list of contact emails (default None)
            string rule - Query used for filtering. (default None)
            IEnumerable<string> listOfEmails -  (default None)
            bool uploadContacts -  (default False)
            bool updateStatus - Should the existing contacts' status be changed automatically based on the validation results (default False)
        Returns string
        """
        attachments = []
        for name in emails:
            attachments.append(('attachments', open(name, 'rb')))

        parameters = { 
                    'rule': rule,
                    'listOfEmails': ";".join(map(str, listOfEmails)),
                    'uploadContacts': uploadContacts,
                    'updateStatus': updateStatus}

        return ApiClient.Request('POST', '/email/verifylist', parameters, attachments)

    def View(messageID, enableTracking = False):
        """
        View email
            string messageID - Message identifier
            bool enableTracking -  (default False)
        Returns ApiTypes.EmailView
        """
        parameters = { 
                    'messageID': messageID,
                    'enableTracking': enableTracking}

        return ApiClient.Request('GET', '/email/view', parameters)


""" 
Manage all of the exported data from the system.
"""
class Export:

    def CheckStatus(publicExportID):
        """
        Check the current status of the export.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            Guid publicExportID - ID of the exported file
        Returns ApiTypes.ExportStatus
        """
        parameters = { 
                    'publicExportID': publicExportID}

        return ApiClient.Request('GET', '/export/checkstatus', parameters)

    def Delete(publicExportID):
        """
        Delete the specified export.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            Guid publicExportID - ID of the exported file
        """
        parameters = { 
                    'publicExportID': publicExportID}

        return ApiClient.Request('GET', '/export/delete', parameters)

    def DownloadBulk(publicExportIDs):
        """
        Download the specified export files in one package
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<Guid> publicExportIDs - 
        Returns File
        """
        parameters = { 
                    'publicExportIDs': ";".join(map(str, publicExportIDs))}

        return ApiClient.Request('GET', '/export/downloadbulk', parameters)

    def List(limit = 0, offset = 0):
        """
        Returns a list of all exported data.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int limit - Maximum number of returned items. (default 0)
            int offset - How many items should be returned ahead. (default 0)
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
        Permanently deletes the file from your Account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int? fileID - Unique identifier for the file stored in your Account. (default None)
            string filename - Name of your file including extension. (default None)
        """
        parameters = { 
                    'fileID': fileID,
                    'filename': filename}

        return ApiClient.Request('GET', '/file/delete', parameters)

    def Download(filename = None, fileID = None):
        """
        Downloads the file to your local device.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string filename - Name of your file including extension. (default None)
            int? fileID - Unique identifier for the file stored in your Account. (default None)
        Returns File
        """
        parameters = { 
                    'filename': filename,
                    'fileID': fileID}

        return ApiClient.Request('GET', '/file/download', parameters)

    def ListAll():
        """
        Lists all your available files.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.File>
        """

        return ApiClient.Request('GET', '/file/listall', parameters)

    def Load(filename):
        """
        Returns detailed file information for the given file.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string filename - Name of your file including extension.
        Returns ApiTypes.File
        """
        parameters = { 
                    'filename': filename}

        return ApiClient.Request('GET', '/file/load', parameters)

    def Upload(file, name = None, expiresAfterDays = 35, enforceUniqueFileName = False):
        """
        Uploads selected file to your Account using http form upload format (MIME multipart/form-data) or PUT method.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            File file - 
            string name - Filename (default None)
            int? expiresAfterDays - Number of days the file should be stored for. (default 35)
            bool enforceUniqueFileName - If a file exists with the same name do not upload and override the file. (default False)
        Returns ApiTypes.File
        """
        attachments = []
        for name in file:
            attachments.append(('attachments', open(name, 'rb')))

        parameters = { 
                    'name': name,
                    'expiresAfterDays': expiresAfterDays,
                    'enforceUniqueFileName': enforceUniqueFileName}

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
            string fileName - Name of your file including extension. (default None)
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

    def Events(statuses = {}, EEfrom = None, to = None, channelName = None, limit = 0, offset = 0):
        """
        Returns log of delivery events filtered by specified parameters.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<ApiTypes.LogEventStatus> statuses - List of comma separated message statuses: 0 for all, 1 for ReadyToSend, 2 for InProgress, 4 for Bounced, 5 for Sent, 6 for Opened, 7 for Clicked, 8 for Unsubscribed, 9 for Abuse Report (default None)
            DateTime? from - Starting date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - Ending date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            string channelName - Name of selected channel. (default None)
            int limit - Maximum number of returned items. (default 0)
            int offset - How many items should be returned ahead. (default 0)
        Returns ApiTypes.EventLog
        """
        parameters = { 
                    'statuses': ";".join(map(str, statuses)),
                    'from': EEfrom,
                    'to': to,
                    'channelName': channelName,
                    'limit': limit,
                    'offset': offset}

        return ApiClient.Request('GET', '/log/events', parameters)

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
            string fileName - Name of your file including extension. (default None)
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

    def ExportEvents(statuses = {}, EEfrom = None, to = None, channelName = None, fileFormat = ApiTypes.ExportFileFormats.Csv, compressionFormat = ApiTypes.CompressionFormat.EENone, fileName = None):
        """
        Export delivery events log information to the specified file format.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<ApiTypes.LogEventStatus> statuses - List of comma separated message statuses: 0 for all, 1 for ReadyToSend, 2 for InProgress, 4 for Bounced, 5 for Sent, 6 for Opened, 7 for Clicked, 8 for Unsubscribed, 9 for Abuse Report (default None)
            DateTime? from - Starting date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - Ending date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            string channelName - Name of selected channel. (default None)
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file including extension. (default None)
        Returns ApiTypes.ExportLink
        """
        parameters = { 
                    'statuses': ";".join(map(str, statuses)),
                    'from': EEfrom,
                    'to': to,
                    'channelName': channelName,
                    'fileFormat': fileFormat.value,
                    'compressionFormat': compressionFormat.value,
                    'fileName': fileName}

        return ApiClient.Request('GET', '/log/exportevents', parameters)

    def ExportLinkTracking(EEfrom, to, channelName = None, fileFormat = ApiTypes.ExportFileFormats.Csv, limit = 0, offset = 0, compressionFormat = ApiTypes.CompressionFormat.EENone, fileName = None):
        """
        Export detailed link tracking information to the specified file format.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            DateTime? from - Starting date for search in YYYY-MM-DDThh:mm:ss format.
            DateTime? to - Ending date for search in YYYY-MM-DDThh:mm:ss format.
            string channelName - Name of selected channel. (default None)
            ApiTypes.ExportFileFormats fileFormat - Format of the exported file (default ApiTypes.ExportFileFormats.Csv)
            int limit - Maximum number of returned items. (default 0)
            int offset - How many items should be returned ahead. (default 0)
            ApiTypes.CompressionFormat compressionFormat - FileResponse compression format. None or Zip. (default ApiTypes.CompressionFormat.EENone)
            string fileName - Name of your file including extension. (default None)
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
            int limit - Maximum number of returned items. (default 0)
            int offset - How many items should be returned ahead. (default 0)
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

    def Load(statuses, EEfrom = None, to = None, channelName = None, limit = 0, offset = 0, includeEmail = True, includeSms = True, messageCategory = {}, email = None, ipaddress = None):
        """
        Returns logs filtered by specified parameters.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<ApiTypes.LogJobStatus> statuses - List of comma separated message statuses: 0 for all, 1 for ReadyToSend, 2 for InProgress, 4 for Bounced, 5 for Sent, 6 for Opened, 7 for Clicked, 8 for Unsubscribed, 9 for Abuse Report
            DateTime? from - Starting date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - Ending date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            string channelName - Name of selected channel. (default None)
            int limit - Maximum number of returned items. (default 0)
            int offset - How many items should be returned ahead. (default 0)
            bool includeEmail - True: Search includes emails. Otherwise, false. (default True)
            bool includeSms - True: Search includes SMS. Otherwise, false. (default True)
            IEnumerable<ApiTypes.MessageCategory> messageCategory - ID of message category (default None)
            string email - Proper email address. (default None)
            string ipaddress - Search for recipients that we sent through this IP address (default None)
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
                    'ipaddress': ipaddress}

        return ApiClient.Request('GET', '/log/load', parameters)

    def LoadNotifications(statuses, EEfrom = None, to = None, limit = 0, offset = 0, messageCategory = {}, useStatusChangeDate = False, notificationType = ApiTypes.NotificationType.All):
        """
        Returns notification logs filtered by specified parameters.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<ApiTypes.LogJobStatus> statuses - List of comma separated message statuses: 0 for all, 1 for ReadyToSend, 2 for InProgress, 4 for Bounced, 5 for Sent, 6 for Opened, 7 for Clicked, 8 for Unsubscribed, 9 for Abuse Report
            DateTime? from - Starting date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            DateTime? to - Ending date for search in YYYY-MM-DDThh:mm:ss format. (default None)
            int limit - Maximum number of returned items. (default 0)
            int offset - How many items should be returned ahead. (default 0)
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
            string fileName - Name of your file including extension. (default None)
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
Send SMS text messages to your clients.
"""
class SMS:

    def Send(to, body):
        """
        Send a short SMS Message (maximum of 1600 characters) to any mobile phone.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string to - Mobile number you want to message. Can be any valid mobile number in E.164 format. To provide the country code you need to provide "+" before the number.  If your URL is not encoded then you need to replace the "+" with "%2B" instead.
            string body - Body of your message. The maximum body length is 160 characters.  If the message body is greater than 160 characters it is split into multiple messages and you are charged per message for the number of messages required to send your length
        """
        parameters = { 
                    'to': to,
                    'body': body}

        return ApiClient.Request('GET', '/sms/send', parameters)


""" 
Managing and editing templates of your emails
"""
class Template:

    def Add(name, subject, fromEmail, fromName, templateScope = ApiTypes.TemplateScope.Private, bodyHtml = None, bodyText = None, css = None, originalTemplateID = 0, tags = {}, bodyAmp = None):
        """
        Create new Template. Needs to be sent using POST method
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string name - Filename
            string subject - Default subject of email.
            string fromEmail - Default From: email address.
            string fromName - Default From: name.
            ApiTypes.TemplateScope templateScope - Enum: 0 - private, 1 - public, 2 - mockup (default ApiTypes.TemplateScope.Private)
            string bodyHtml - HTML code of email (needs escaping). (default None)
            string bodyText - Text body of email. (default None)
            string css - CSS style (default None)
            int originalTemplateID - ID number of original template. (default 0)
            IEnumerable<string> tags -  (default None)
            string bodyAmp - AMP code of email (needs escaping). (default None)
        Returns int
        """
        parameters = { 
                    'name': name,
                    'subject': subject,
                    'fromEmail': fromEmail,
                    'fromName': fromName,
                    'templateScope': templateScope.value,
                    'bodyHtml': bodyHtml,
                    'bodyText': bodyText,
                    'css': css,
                    'originalTemplateID': originalTemplateID,
                    'tags': ";".join(map(str, tags)),
                    'bodyAmp': bodyAmp}

        return ApiClient.Request('GET', '/template/add', parameters)

    def AddTag(tag):
        """
        Create a new Tag to be used in your Templates
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string tag - Tag's value
        Returns ApiTypes.TemplateTag
        """
        parameters = { 
                    'tag': tag}

        return ApiClient.Request('GET', '/template/addtag', parameters)

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

    def DeleteBulk(templateIDs):
        """
        Delete templates with the specified ID
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<int> templateIDs - 
        """
        parameters = { 
                    'templateIDs': ";".join(map(str, templateIDs))}

        return ApiClient.Request('GET', '/template/deletebulk', parameters)

    def DeleteTag(tag):
        """
        Delete a tag, removing it from all Templates
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string tag - 
        """
        parameters = { 
                    'tag': tag}

        return ApiClient.Request('GET', '/template/deletetag', parameters)

    def GetList(tags = {}, templateTypes = {}, limit = 500, offset = 0):
        """
        Lists your templates, optionally searching by Tags
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<string> tags -  (default None)
            IEnumerable<ApiTypes.TemplateType> templateTypes -  (default None)
            int limit - If provided, returns templates with these tags (default 500)
            int offset - Filters on template type (default 0)
        Returns ApiTypes.TemplateList
        """
        parameters = { 
                    'tags': ";".join(map(str, tags)),
                    'templateTypes': ";".join(map(str, templateTypes)),
                    'limit': limit,
                    'offset': offset}

        return ApiClient.Request('GET', '/template/getlist', parameters)

    def GetTagList():
        """
        Retrieve a list of your Tags
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns ApiTypes.TemplateTagList
        """

        return ApiClient.Request('GET', '/template/gettaglist', parameters)

    def IsUsedByCampaign(templateID):
        """
        Check if template is used by campaign.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int templateID - ID number of template.
        Returns bool
        """
        parameters = { 
                    'templateID': templateID}

        return ApiClient.Request('GET', '/template/isusedbycampaign', parameters)

    def LoadTemplate(templateID):
        """
        Load template with content
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int templateID - ID number of template.
        Returns ApiTypes.Template
        """
        parameters = { 
                    'templateID': templateID}

        return ApiClient.Request('GET', '/template/loadtemplate', parameters)

    def ReadRssFeed(url, count = 3):
        """
        Read Rss feed
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string url - Rss feed url.
            int count - Number of item tags to read. (default 3)
        Returns string
        """
        parameters = { 
                    'url': url,
                    'count': count}

        return ApiClient.Request('GET', '/template/readrssfeed', parameters)

    def Update(templateID, templateScope = ApiTypes.TemplateScope.Private, name = None, subject = None, fromEmail = None, fromName = None, bodyHtml = None, bodyText = None, css = None, removeScreenshot = True, tags = {}, bodyAmp = None):
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
            IEnumerable<string> tags -  (default None)
            string bodyAmp - AMP code of email (needs escaping). (default None)
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
                    'removeScreenshot': removeScreenshot,
                    'tags': ";".join(map(str, tags)),
                    'bodyAmp': bodyAmp}

        return ApiClient.Request('GET', '/template/update', parameters)

    def UpdateDefaultOptions(templateIDs, subject = None, fromEmail = None, fromName = None, templateScope = ApiTypes.TemplateScope.Private):
        """
        Bulk change default options and the scope of your templates
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            IEnumerable<int> templateIDs - 
            string subject - Default subject of email. (default None)
            string fromEmail - Default From: email address. (default None)
            string fromName - Default From: name. (default None)
            ApiTypes.TemplateScope templateScope - Enum: 0 - private, 1 - public, 2 - mockup (default ApiTypes.TemplateScope.Private)
        """
        parameters = { 
                    'templateIDs': ";".join(map(str, templateIDs)),
                    'subject': subject,
                    'fromEmail': fromEmail,
                    'fromName': fromName,
                    'templateScope': templateScope.value}

        return ApiClient.Request('GET', '/template/updatedefaultoptions', parameters)


""" 
Managing sender emails.
"""
class ValidEmail:

    def Add(emailAddress, returnUrl = None):
        """
        Add new email to account
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string emailAddress - 
            string returnUrl - URL to navigate to after Account creation (default None)
        Returns ApiTypes.ValidEmail
        """
        parameters = { 
                    'emailAddress': emailAddress,
                    'returnUrl': returnUrl}

        return ApiClient.Request('GET', '/validemail/add', parameters)

    def List():
        """
        Get list of all valid emails of account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
        Returns List<ApiTypes.ValidEmail>
        """

        return ApiClient.Request('GET', '/validemail/list', parameters)

    def Remove(validEmailID):
        """
        Delete valid email from account.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            int validEmailID - 
        """
        parameters = { 
                    'validEmailID': validEmailID}

        return ApiClient.Request('GET', '/validemail/remove', parameters)

    def ResendEmailVerification(emailAddress, returnUrl = None):
        """
        Resends email verification.
            string apikey - ApiKey that gives you access to our SMTP and HTTP API's.
            string emailAddress - 
            string returnUrl - URL to navigate to after Account creation (default None)
        """
        parameters = { 
                    'emailAddress': emailAddress,
                    'returnUrl': returnUrl}

        return ApiClient.Request('GET', '/validemail/resendemailverification', parameters)

