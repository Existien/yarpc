/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/qt6/06_enums.yml
 *   Template: qt6/object_path_source.j2
 */
#include "Connection.hpp"
#include "EnumsInterface.hpp"
#include "EnumsWithArraysInterface.hpp"
#include "EnumsWithDictsInterface.hpp"

using namespace gen::enums;


EnumsTestserviceYarpcComObjectPath::EnumsTestserviceYarpcComObjectPath(QObject *parent) : QObject(parent) {
}

bool EnumsTestserviceYarpcComObjectPath::hasRegistrations() const {
    return (
        false
        || m_enums != nullptr
        || m_enumsWithArrays != nullptr
        || m_enumsWithDicts != nullptr
    );
}


Connection::Connection() : QObject(nullptr) {}

Connection& Connection::instance() {
    static Connection object{};
    return object;
}

void Connection::connect() {
    bool hasChanged = false;
    if (m_connection == nullptr) {
        m_connection = std::make_unique<QDBusConnection>(QDBusConnection::connectToBus(QDBusConnection::SessionBus, "com.yarpc.testservice"));
        if ( m_connection->isConnected()) {
            m_connection->registerService("com.yarpc.testservice");
            hasChanged = true;
        }
    }

    if (hasChanged) {
        emit connectedChanged();
    }
}

void Connection::disconnect(){
    if (m_connection == nullptr) {
        return;
    }
    m_connection->disconnectFromBus("com.yarpc.testservice");
    m_connection = nullptr;
    emit connectedChanged();
}

void Connection::disconnectIfUnused(){
    if (
        false
        || m_Enums != nullptr
        || m_EnumsWithArrays != nullptr
        || m_EnumsWithDicts != nullptr
    ) {
        return;
    }
    disconnect();
}

void Connection::updateRegistrations() {
    if (m_connection != nullptr && m_connection->isConnected()) {
        m_connection->unregisterObject("/com/yarpc/testservice/enums");
        m_EnumsTestserviceYarpcComObjectPath.reset(new EnumsTestserviceYarpcComObjectPath(this));
        if (m_Enums != nullptr) {
            auto enumsInterface = dynamic_cast<EnumsInterface*>(m_Enums);
            m_EnumsTestserviceYarpcComObjectPath->m_enums = new EnumsInterfaceAdaptor(
                enumsInterface,
                m_EnumsTestserviceYarpcComObjectPath.get()
            );
        }
        if (m_EnumsWithArrays != nullptr) {
            auto enumsWithArraysInterface = dynamic_cast<EnumsWithArraysInterface*>(m_EnumsWithArrays);
            m_EnumsTestserviceYarpcComObjectPath->m_enumsWithArrays = new EnumsWithArraysInterfaceAdaptor(
                enumsWithArraysInterface,
                m_EnumsTestserviceYarpcComObjectPath.get()
            );
        }
        if (m_EnumsWithDicts != nullptr) {
            auto enumsWithDictsInterface = dynamic_cast<EnumsWithDictsInterface*>(m_EnumsWithDicts);
            m_EnumsTestserviceYarpcComObjectPath->m_enumsWithDicts = new EnumsWithDictsInterfaceAdaptor(
                enumsWithDictsInterface,
                m_EnumsTestserviceYarpcComObjectPath.get()
            );
        }
        if (
            false
            || m_Enums != nullptr
            || m_EnumsWithArrays != nullptr
            || m_EnumsWithDicts != nullptr
        ) {
            m_connection->registerObject(
                "/com/yarpc/testservice/enums",
                m_EnumsTestserviceYarpcComObjectPath.get()
            );
        }
        emit registrationChanged();
    }
}

bool Connection::getConnected() const {
    return m_connection != nullptr;
}

void Connection::send(const QDBusMessage &message) {
    if (m_connection == nullptr) {
        qDebug() << "Sending message failed: No connection";
        return;
    }
    m_connection->send(message);
}

void Connection::registerEnums(QObject* interface) {
    if (m_Enums == nullptr) {
        auto enumsInterface = dynamic_cast<EnumsInterface*>(interface);
        if (enumsInterface != nullptr) {
            m_Enums = interface;
        }
    }
    connect();
    updateRegistrations();
}

void Connection::unregisterEnums() {
    if (m_Enums != nullptr) {
        m_Enums = nullptr;
    }
    updateRegistrations();
    disconnectIfUnused();
}

bool Connection::isEnumsRegistered() const {
    return (m_Enums != nullptr);
}

EnumsInterfaceAdaptor* Connection::Enums() {
    if (m_EnumsTestserviceYarpcComObjectPath != nullptr) {
        return m_EnumsTestserviceYarpcComObjectPath->m_enums;
    } else {
        return nullptr;
    }
}

void Connection::registerEnumsWithArrays(QObject* interface) {
    if (m_EnumsWithArrays == nullptr) {
        auto enumsWithArraysInterface = dynamic_cast<EnumsWithArraysInterface*>(interface);
        if (enumsWithArraysInterface != nullptr) {
            m_EnumsWithArrays = interface;
        }
    }
    connect();
    updateRegistrations();
}

void Connection::unregisterEnumsWithArrays() {
    if (m_EnumsWithArrays != nullptr) {
        m_EnumsWithArrays = nullptr;
    }
    updateRegistrations();
    disconnectIfUnused();
}

bool Connection::isEnumsWithArraysRegistered() const {
    return (m_EnumsWithArrays != nullptr);
}

EnumsWithArraysInterfaceAdaptor* Connection::EnumsWithArrays() {
    if (m_EnumsTestserviceYarpcComObjectPath != nullptr) {
        return m_EnumsTestserviceYarpcComObjectPath->m_enumsWithArrays;
    } else {
        return nullptr;
    }
}

void Connection::registerEnumsWithDicts(QObject* interface) {
    if (m_EnumsWithDicts == nullptr) {
        auto enumsWithDictsInterface = dynamic_cast<EnumsWithDictsInterface*>(interface);
        if (enumsWithDictsInterface != nullptr) {
            m_EnumsWithDicts = interface;
        }
    }
    connect();
    updateRegistrations();
}

void Connection::unregisterEnumsWithDicts() {
    if (m_EnumsWithDicts != nullptr) {
        m_EnumsWithDicts = nullptr;
    }
    updateRegistrations();
    disconnectIfUnused();
}

bool Connection::isEnumsWithDictsRegistered() const {
    return (m_EnumsWithDicts != nullptr);
}

EnumsWithDictsInterfaceAdaptor* Connection::EnumsWithDicts() {
    if (m_EnumsTestserviceYarpcComObjectPath != nullptr) {
        return m_EnumsTestserviceYarpcComObjectPath->m_enumsWithDicts;
    } else {
        return nullptr;
    }
}

