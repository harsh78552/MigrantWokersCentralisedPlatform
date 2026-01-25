const translations = {
    en: {
        // DASHBOARD
        dashboard: "Patient Dashboard",
        health_card: "My Health Card",
        records: "My Records",
        doctor_visits: "Doctor Visits",
        emergency: "Emergency",
        language: "Language",
        profile: "My Profile",
        help: "Help",

        // HELP PAGE
        help_title: "Help & Support",
        contact_support: "Contact Support",
        emergency_guidance: "Emergency Guidance",
        faq: "Frequently Asked Questions",
        report_issue: "Report an Issue",
        app_info: "App Information",
        submit: "Submit"
    },

    hi: {
        // DASHBOARD
        dashboard: "रोगी डैशबोर्ड",
        health_card: "स्वास्थ्य कार्ड",
        records: "मेरे रिकॉर्ड",
        doctor_visits: "डॉक्टर विज़िट",
        emergency: "आपातकाल",
        language: "भाषा",
        profile: "मेरी प्रोफ़ाइल",
        help: "सहायता",

        // HELP PAGE
        help_title: "सहायता एवं समर्थन",
        contact_support: "संपर्क सहायता",
        emergency_guidance: "आपातकालीन मार्गदर्शन",
        faq: "अक्सर पूछे जाने वाले प्रश्न",
        report_issue: "समस्या रिपोर्ट करें",
        app_info: "ऐप जानकारी",
        submit: "जमा करें"
    },

    ml: {
        // DASHBOARD
        dashboard: "രോഗിയുടെ ഡാഷ്ബോർഡ്",
        health_card: "ആരോഗ്യ കാർഡ്",
        records: "എന്റെ രേഖകൾ",
        doctor_visits: "ഡോക്ടർ സന്ദർശനം",
        emergency: "അത്യാഹിതം",
        language: "ഭാഷ",
        profile: "എന്റെ പ്രൊഫൈൽ",
        help: "സഹായം",

        // HELP PAGE
        help_title: "സഹായവും പിന്തുണയും",
        contact_support: "സഹായം ബന്ധപ്പെടുക",
        emergency_guidance: "അത്യാഹിത മാർഗ്ഗനിർദ്ദേശങ്ങൾ",
        faq: "പതിവുചോദ്യങ്ങൾ",
        report_issue: "പ്രശ്നം റിപ്പോർട്ട് ചെയ്യുക",
        app_info: "ആപ്പ് വിവരം",
        submit: "സമർപ്പിക്കുക"
    }
};


function setText(id, value) {
    const el = document.getElementById(id);
    if (el && value) {
        el.innerText = value;
    }
}


function applyLanguage() {
    const lang = localStorage.getItem("language") || "en";
    const t = translations[lang];
    if (!t) return;

    /* DASHBOARD */
    setText("txt-dashboard", t.dashboard);
    setText("txt-health-card", t.health_card);
    setText("txt-records", t.records);
    setText("txt-doctor-visits", t.doctor_visits);
    setText("txt-emergency", t.emergency);
    setText("txt-language", t.language);
    setText("txt-profile", t.profile);
    setText("txt-help", t.help);

    /* HELP PAGE */
    setText("txt-help-title", t.help_title);
    setText("txt-help-header", t.help_title);
    setText("txt-contact-support", t.contact_support);
    setText("txt-emergency-guidance", t.emergency_guidance);
    setText("txt-faq", t.faq);
    setText("txt-report-issue", t.report_issue);
    setText("txt-app-info", t.app_info);
    setText("txt-submit", t.submit);
}
