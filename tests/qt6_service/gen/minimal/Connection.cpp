/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/qt6/01_minimal.yml
 *   Template: qt6/object_path_source.j2
 */
#include "Connection.hpp"
#include "MinimalInterface.hpp"

using namespace gen::minimal;


MinimalTestserviceYarpcComObjectPath::MinimalTestserviceYarpcComObjectPath(QObject *parent) : QObject(parent) {
}

bool MinimalTestserviceYarpcComObjectPath::hasRegistrations() const {
    return (
        false
        || m_minimal != nullptr
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
        || m_Minimal != nullptr
    ) {
        return;
    }
    disconnect();
}

void Connection::updateRegistrations() {
    if (m_connection != nullptr && m_connection->isConnected()) {
        m_connection->unregisterObject("/com/yarpc/testservice/minimal");
        m_MinimalTestserviceYarpcComObjectPath.reset(new MinimalTestserviceYarpcComObjectPath(this));
        if (m_Minimal != nullptr) {
            auto minimalInterface = dynamic_cast<MinimalInterface*>(m_Minimal);
            m_MinimalTestserviceYarpcComObjectPath->m_minimal = new MinimalInterfaceAdaptor(
                minimalInterface,
                m_MinimalTestserviceYarpcComObjectPath.get()
            );
        }
        if (
            false
            || m_Minimal != nullptr
        ) {
            m_connection->registerObject(
                "/com/yarpc/testservice/minimal",
                m_MinimalTestserviceYarpcComObjectPath.get()
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

void Connection::registerMinimal(QObject* interface) {
    if (m_Minimal == nullptr) {
        auto minimalInterface = dynamic_cast<MinimalInterface*>(interface);
        if (minimalInterface != nullptr) {
            m_Minimal = interface;
        }
    }
    connect();
    updateRegistrations();
}

void Connection::unregisterMinimal() {
    if (m_Minimal != nullptr) {
        m_Minimal = nullptr;
    }
    updateRegistrations();
    disconnectIfUnused();
}

bool Connection::isMinimalRegistered() const {
    return (m_Minimal != nullptr);
}

MinimalInterfaceAdaptor* Connection::Minimal() {
    if (m_MinimalTestserviceYarpcComObjectPath != nullptr) {
        return m_MinimalTestserviceYarpcComObjectPath->m_minimal;
    } else {
        return nullptr;
    }
}

